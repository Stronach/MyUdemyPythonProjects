def con():
    f = float(c) * 9/5 + 32
    return f

c = float(input("Enter Temp: "))
if c < float(-273.15):
    print("That's not possible")
else:

    print(con())
