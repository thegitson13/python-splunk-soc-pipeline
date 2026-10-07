
class Config:

    USERS = {
        "jan.kowalski": {
            "host": "FIN-PC-01",
            "ip": "10.0.0.10",
            "department": "Finance"
        },

        "anna.nowak": {
            "host": "HR-PC-01",
            "ip": "10.0.0.11",
            "department": "HR"
        },

        "tomasz.wisniewski": {
            "host": "IT-PC-01",
            "ip": "10.0.0.12",
            "department": "IT"
        },

        "karolina.wojcik": {
            "host": "SALES-PC-01",
            "ip": "10.0.0.13",
            "department": "Sales"
        },

        "piotr.kaminski": {
            "host": "MKT-PC-01",
            "ip": "10.0.0.14",
            "department": "Marketing"
        }
    }

    NORMAL_PROCESSES = [
        "chrome.exe",
        "msedge.exe",
        "outlook.exe",
        "teams.exe",
        "excel.exe",
        "winword.exe",
        "notepad.exe",
        "explorer.exe"
    ]

    NORMAL_POWERSHELL_COMMANDS = [
        "powershell.exe Get-Date",
        "powershell.exe Get-Process",
        "powershell.exe Get-Service"
    ]

    SUSPICIOUS_POWERSHELL_COMMANDS = [
        "powershell.exe -ExecutionPolicy Bypass -Command Get-Process",
        "powershell.exe -WindowStyle Hidden -Command Get-Service",
        "powershell.exe -EncodedCommand SQBFAFgA"
    ]

    NORMAL_DESTINATIONS = [
        {
            "domain": "microsoft.com",
            "ip": "192.0.2.10",
            "port": 443
        },

        {
            "domain": "office.com",
            "ip": "192.0.2.11",
            "port": 443
        },

        {
            "domain": "github.com",
            "ip": "192.0.2.12",
            "port": 443
        },

        {
            "domain": "google.com",
            "ip": "192.0.2.13",
            "port": 443
        }
    ]

    ATTACKER_IPS = [
        "203.0.113.50",
        "203.0.113.75",
        "198.51.100.40"
    ]


    SUSPICIOUS_DESTINATIONS = [
        {
            "ip": "198.51.100.77",
            "port": 4444
        },

        {
            "ip": "203.0.113.99",
            "port": 8080
        }
    ]

    PROTOCOLS = [
        "TCP",
        "UDP"
    ]

    LOGIN_FAILURE_REASONS = [
        "bad_password",
        "unknown_user",
        "account_locked",
        "expired_password"
    ]