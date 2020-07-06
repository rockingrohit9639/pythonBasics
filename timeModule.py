import time
from os import system
while True:
    # current_time = time.ctime(time.time())
    # current_time = time.gmtime(time.time())
    current_time = time.ctime(time.time())
    print(current_time)
    time.sleep(1)
    # if current_time.tm_sec == 10:
    #     break