def c_to_f(c):
    if c < -273.15:
        return "That temperature doesn't make sense!"
    else:
        f = c * 9/5 +32
        return f

temperatures = [10, -20, -289, 100]
file = open("temp.txt", 'w')

for c in temperatures:
    print(c_to_f(c))
    file.write(str(c_to_f(c)))
    file.write("\n")

file.close()
