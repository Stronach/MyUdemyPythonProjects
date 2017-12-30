# blocker.py

import time
from datetime import datetime as dt


n = dt.now().year,dt.now().month,dt.now().day
host = "/etc/hosts"
hosttemp="hosts"
redirect="127.0.0.1"
weblist=["facebook.com","www.facebook.com","wibx950.com", "www.wibx950.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day, 8) < dt.now() <dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working Hours")
        with open(host,'r+') as file:
            content = file.read()
            #print(content)
            for website in weblist:
                if website in content:
                    pass
                else:
                    file.write(redirect+" " + website + "\n")
    else:
        print("Fun Hours")
        with open(host, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in weblist):
                    file.write(line)
            file.truncate()
            #print(content)

    time.sleep(5)
