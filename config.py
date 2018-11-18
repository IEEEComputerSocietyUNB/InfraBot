import os
from configparser import ConfigParser


def get_token(section="MAIN", filename="config.ini"):
    """
    Function to retrieve all informations from token file.
    Usually retrieves from config.ini
    """
    try:
        FILE_PATH = f"{filename}"
        config = ConfigParser()
        with open(FILE_PATH) as config_file:
            config.read_file(config_file)
        return(config[section])
    except FileNotFoundError:
        print("Não há arquivo de configuração, verificar 'config_sample.ini'")
        raise FileNotFoundError
