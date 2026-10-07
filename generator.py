import random
from datetime import datetime, timezone, timedelta

class Generator:
    def __init__(self, data):
        self.data = data


    def _random_user(self):
        random_user = random.choice(list(self.data.USERS.keys()))
        more_accurate_data = self.data.USERS[random_user]

        return random_user, more_accurate_data


    def _random_timestamp(self):
        now = datetime.now(timezone.utc)
        random_time = now - timedelta(seconds=random.randint(0, 3600))

        return random_time


    def successful_login(self):

        success_logins = []
        number_of_logins = random.choice(range(1, 91))

        for _ in range(number_of_logins):

            username, user_data  = self._random_user()
            time = self._random_timestamp()

            success_logins.append({
                    "timestamp": time.isoformat(),
                    "event_type": "successful_login",
                    "user": username,
                    "host": user_data["host"],
                    "src_ip": user_data["ip"],
                    "department": user_data["department"],
                    "status": "success"
                })
            
        return success_logins
    
    
    def failed_login(self):

        failed_login = []
        number_of_logins = random.choice(range(1, 31))
        number_of_failed_logins = random.choice(range(1, 11))

        for _ in range(number_of_logins):

            random_reason = random.choice(self.data.LOGIN_FAILURE_REASONS)
            
            username, user_data = self._random_user()
            time = self._random_timestamp()

            failed_login.append({     
                    "timestamp": time.isoformat(),
                    "event_type": "failed_login",
                    "user": username,
                    "host": user_data["host"],
                    "src_ip": user_data["ip"],
                    "department": user_data["department"],
                    "status": "failure",
                    "failure_reason": random_reason
                })

        for _ in range(number_of_failed_logins):

            random_reason = random.choice(self.data.LOGIN_FAILURE_REASONS)

            random_attacker_ip = random.choice(self.data.ATTACKER_IPS)

            username, user_data = self._random_user()
            time = self._random_timestamp()

            failed_login.append({     
                    "timestamp": time.isoformat(),
                    "event_type": "failed_login",
                    "user": username,
                    "host": user_data["host"],
                    "src_ip": random_attacker_ip,
                    "department": user_data["department"],
                    "status": "failure",
                    "failure_reason": random_reason
                })
            
        return failed_login
    
            
    def process_start(self):

        process_list = []

        number_of_processes = random.choice(range(1, 136))
        number_of_processes_ps = random.choice(range(1, 71))

        for _ in range(number_of_processes):

            random_process = random.choice(self.data.NORMAL_PROCESSES)

            username, user_data = self._random_user()
            time = self._random_timestamp()

            process_list.append({
                    "timestamp": time.isoformat(),
                    "event_type": "process_start",
                    "user": username,
                    "host": user_data["host"],
                    "process": random_process,
                    "command_line": random_process,
                    "status": "success"
                })

        for _ in range(number_of_processes_ps):

            username, user_data = self._random_user()
            time = self._random_timestamp()

            random_normal_command = random.choice(self.data.NORMAL_POWERSHELL_COMMANDS)
            random_sus_command = random.choice(self.data.SUSPICIOUS_POWERSHELL_COMMANDS)
            sus_choice = random.randint(1, 2)

            if sus_choice % 2 == 0:
                process_list.append({
                        "timestamp": time.isoformat(),
                        "event_type": "process_start",
                        "user": username,
                        "host": user_data["host"],
                        "process": "powershell.exe",
                        "command_line": random_sus_command,
                        "status": "success"
                    })
            else:
                process_list.append({
                        "timestamp": time.isoformat(),
                        "event_type": "process_start",
                        "user": username,
                        "host": user_data["host"],
                        "process": "powershell.exe",
                        "command_line": random_normal_command,
                        "status": "success"
                    })

        return process_list
    
        
    def network_connection(self):

        net_connection = []

        number_of_net_connections = random.choice(range(1, 401))

        for _ in range(number_of_net_connections):

            random_destination = random.choice(self.data.NORMAL_DESTINATIONS)
            random_protocols = random.choice(self.data.PROTOCOLS)
            random_sus_destination = random.choice(self.data.SUSPICIOUS_DESTINATIONS)

            username, user_data = self._random_user()
            time = self._random_timestamp()

            sus_choice = random.randint(1, 2)

            if sus_choice % 2 == 0:
                net_connection.append({
                        "timestamp": time.isoformat(),
                        "event_type": "network_connection",
                        "user": username,
                        "host": user_data["host"],
                        "src_ip": user_data["ip"],
                        "domain": random_destination["domain"],
                        "dest_ip": random_destination["ip"],
                        "dest_port": random_destination["port"],
                        "protocol": random_protocols,
                        "status": "allowed"
                    })
            else:
                net_connection.append({
                        "timestamp": time.isoformat(),
                        "event_type": "network_connection",
                        "user": username,
                        "host": user_data["host"],
                        "src_ip": user_data["ip"],
                        "dest_ip": random_sus_destination["ip"],
                        "dest_port": random_sus_destination["port"],
                        "protocol": random_protocols,
                        "status": "allowed"
                    })

        return net_connection

