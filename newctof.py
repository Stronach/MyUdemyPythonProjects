"""
This script takes C and converts to F
"""

temperatures = [10,-20,-289,100]

def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f=c*9/5+32
                file.write(str(f) + "\n")
writer(temperatures)

#def c_to_f(c):
#    if c > -273.15:
#        f=c*9/5+32
#        return f

#for t in temperatures:
#    with open("temps.txt", 'w') as file:
#        #print(c_to_f(t))
#        file.write(str(c_to_f(t))+("\n"))
#        print(c_to_f(t))
    #file.close()
