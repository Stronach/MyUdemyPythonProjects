#time.py

import datetime

filename = datetime.datetime.now()
def create_file():
    """This function creates a file named after the current daytime"""
    with open((filename.strftime("%Y-%m-%d-%H:%M:%S")+".txt"), "w") as file:
        file.write("")

create_file()
