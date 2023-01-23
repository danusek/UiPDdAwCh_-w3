import logging

def get_logs(level, message):
    logging.basicConfig(level=level, format='%(asctime)s: %(levelname)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
    if level == "DEBUG":
        logging.debug(message)
    elif level == "INFO":
        logging.info(message)
    elif level == "WARNING":
        logging.warning(message)
    elif level == "ERROR":
        logging.error(message)
    elif level == "CRITICAL":
        logging.critical(message)
    else:
        return "Nieprawidłowy poziom logowania"

get_logs("WARNING", "To jest komunikat ostrzegawczy")
get_logs("ERROR", "To jest komunikat błędu")