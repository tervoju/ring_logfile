import logging
import time
from datetime import datetime

from logging.handlers import RotatingFileHandler
 
#----------------------------------------------------------------------
def create_rotating_log(path, dt, csv_str):
    """
    Creates a rotating log
    """
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)
     
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=1000, backupCount=1)
    logger.addHandler(handler)
    # Append text at the end of file
    str_str = str(dt) + " "  + csv_str  
    for i in range(100):
        logger.info(str_str + "%s" % i)
        time.sleep(1.5)


# create log file
def create_rotating_file(path, maxsize):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)   
    # add a rotating handler
    handler = RotatingFileHandler(path, maxBytes=1000, backupCount=1)
    logger.addHandler(handler)
    return logger

# add log line to file
def add_ring_logging(logger, dt, csv_str):
    # Append text at the end of file
    str_str = str(dt) + " "  + csv_str  
    logger.info(str_str)
         
#----------------------------------------------------------------------
if __name__ == "__main__":
    # Getting the current date and time
 
    log_file = "test.log"
    #create_rotating_log(log_file, dt, "123,123,123,123,123")
    logger = create_rotating_file(log_file, 1000)
  
    for i in range(100):
        dt = datetime.now()
        add_ring_logging(logger, dt, ",123,123,123,123,123")
        time.sleep(1.5)
