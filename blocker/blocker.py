# blocker.py

import time
from datetime import datetime as dt

n = dt.now().year,dt.now().month,dt.now().day
host = "/etc/hosts"
redirect="127.0.0.1"
whitelist=["facebook.com","www.facebook.com","wibx950.com", "www.wibx950.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("working hours")

    else:
        print("Fun Hours")
    time.sleep(5)
