from tkinter import *

window = Tk()

def convert():
    print(e1_value.get())
    gram = float(e1_value.get())*1000
    t1.delete("1.0", END)
    t1.insert(END,gram)
    
    ounce = float(e1_value.get())*35.274
    t2.delete("1.0", END)
    t2.insert(END,ounce)

    pound = float(e1_value.get())*2.20462
    t3.delete("1.0", END)
    t3.insert(END,pound)

e1=Label(window,text="Kg")
e1.grid(row=0,column=0) 


b1 = Button(window, text ="Execute", command = convert)
b1.grid(row=0, column = 3)

e1_value = StringVar()
e1=Entry(window, textvariable = e1_value)
e1.grid(row=0,column=1)

t1 = Text(window, height = 1, width=20)
t1.grid(row=1,column=0)
t2 = Text(window, height = 1, width=20)
t2.grid(row=1,column=1)
t3 = Text(window, height = 1, width=20)
t3.grid(row=1,column=2)

window.mainloop()
