import logging
import os

def get_logger():
    logger = logging.getLogger("etl-api")
    logger.setLevel(os.getenv("LOG_LEVEL", "INFO"))

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    ))
    logger.addHandler(handler)
    
    return logger