from Tkinter import *
from tkMessageBox import showinfo
my_app = Tk(className='Calculator')

def tambah():
    a=float(str1.get())
    b=float(str2.get())
    c = a+b
    L.config(text = c)

def kurang():
    a=float(str1.get())
    b=float(str2.get())
    c = a-b
    L.config(text = c)

def kali():
    a=float(str1.get())
    b=float(str2.get())
    c = a*b
    L.config(text = c)

def bagi():
    a=float(str1.get())
    b=float(str2.get())
    c = a/b
    L.config(text = c)


L0 = Label(my_app, text="KALKULASI")
L0.grid(row=0, column=0, sticky="w")
L1 = Label(my_app, text="angka1")
L1.grid(row=1, column=0, sticky="w")
str1 = StringVar()
E1 = Entry(my_app, textvariable=str1)
E1.grid(row=1, column=1, sticky="w")
L2 = Label(my_app, text="angka2")
L2.grid(row=3, column=0, sticky="w")
str2 = StringVar()
E2 = Entry(my_app, textvariable=str2)
E2.grid(row=3, column=1)
L3 = Button(my_app, text="+", command=tambah)
L3.grid(row=5, column=2)
L4 = Button(my_app, text="-", command=kurang)
L4.grid(row=5, column=3)
L5 = Button(my_app, text="x", command=kali)
L5.grid(row=5, column=4)
L6 = Button(my_app, text="/", command=bagi)
L6.grid(row=5, column=5,)
L7 = Label(my_app, text="Hasil")
L7.grid(row=7, column=0, sticky="w")


    
    
L = Label(my_app, text='0')
L.grid(row=7, column=1, sticky="w")
my_app.mainloop()
