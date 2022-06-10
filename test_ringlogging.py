from datetime import datetime
import time

from ringlogging import create_rotating_file, add_ring_logging

#----------------------------------------------------------------------
if __name__ == "__main__":
    # Getting the current date and time
 
    log_file = "test.log"
    logger = create_rotating_file(log_file, 1000)
  
    for i in range(100):
        dt = datetime.now()
        add_ring_logging(logger, dt, ",123,123,123,123,123")
        time.sleep(1.5)