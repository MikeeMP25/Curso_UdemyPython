import datetime
import time
import os

while True:
    os.system("clear")
    hoy=datetime.datetime.now()
    print('{}:{}:{}'.format(hoy.hour,hoy.minute,hoy.second))
    time.sleep(1)