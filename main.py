from pathlib import Path
import json
import logging
from data_config import Config
from generator import Generator

PATH_FOR_DATA = Path(__file__).parent /"data/logs.json"

def main(s_login, f_login, proc, net):

    combined_data = []

    combined_data.extend(s_login)
    combined_data.extend(f_login)
    combined_data.extend(proc)
    combined_data.extend(net)
    print(combined_data)

    try:
        with open(PATH_FOR_DATA, "w", encoding="utf-8") as file:
            json.dump(combined_data, file, indent=4)
            print(f"Json file was saved directly in {PATH_FOR_DATA}")
    except IOError as e:
        logging.error(f"Error saving report to {PATH_FOR_DATA}: {e}")

if __name__== "__main__":
    data_config = Config()
    generator = Generator(data_config)
    suc_login = generator.successful_login()
    fail_login = generator.failed_login()
    processes = generator.process_start()
    net_con = generator.network_connection()
    main(suc_login, fail_login, processes, net_con)