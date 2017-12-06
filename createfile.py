import datetime

filename = datetime.datetime.now()
outfile = ["file1.txt", "file2.txt", "file3.txt"]

#def create_file():
"""This function creates a file named after the current daytime"""
with open((filename.strftime("%Y-%m-%d-%H:%M:%S")+".txt"), "w") as file:
    for f in outfile:
        with open(f) as infile:
            file.write(infile.read()+"\n")


#create_file(lst) #here we're calling the function
