import glob2
import datetime

filename = datetime.datetime.now()
outfile = glob2.glob("file" + "*.txt")

#def create_file():
"""This function creates a file named after the current daytime"""
with open((filename.strftime("%Y-%m-%d-%H:%M:%S")+".txt"), "w") as file:
    for f in outfile:
        with open(f) as infile:
            file.write(infile.read()+"\n")


#create_file(lst) #here we're calling the function
