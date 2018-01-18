from tkinter import *

window=Tk()

def km_to_miles():
    grams=float(e1_value.get())*1000
    lbs=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t2.delete("1.0", END)
    t2.insert(END, grams)
    t3.delete("1.0", END)
    t3.insert(END, lbs)
    t4.delete("1.0", END)
    t4.insert(END, ounces)

b1=Button(window, text="Convert", command=km_to_miles)
b1.grid(row=0,column=5) #can use b1.pack but there is more control with b1.grid()

e1=Label(window,text="Kg")
e1.grid(row=0,column=3)



e1_value=StringVar()
e1 = Entry(window,width=10, textvariable=e1_value)
e1.grid(row=0, column=4)


t2=Text(window, height=1,width=10)
t2.grid(row=1,column=0)
t2text=Label(window,text="Grams")
t2text.grid(row=1,column=1)

t3=Text(window, height=1, width=10)
t3.grid(row=1,column=2)
t3text=Label(window,text="LBS")
t3text.grid(row=1,column=3)

t4=Text(window, height=1, width=10)
t4.grid(row=1,column=4)
t4text=Label(window,text="Ounces")
t4text.grid(row=1,column=5)

window.mainloop() #This should always be at the end for UI
