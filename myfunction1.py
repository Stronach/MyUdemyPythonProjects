y = input("Enter a Word: ")
if type(y) == int:
    y = str(y)
else:
    y = y
def mystring(y):

    if type(y) == int:
        return "Sorry, integers don't have length in Python."
    elif type(y) == float:
        return "Sorry floats don't have length in Python"

    else:
        y = len(y)
        return y

#mystring(10)(
print(mystring(y))
