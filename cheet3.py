from Tkinter import *
from tkMessageBox import showinfo
my_app = Tk(className='Bangun Persegi')

def luas():
    a = float(str1.get())
    c = a*a
    L5.config(text = c)

L1 = Label(my_app, text="Bangun Persegi", font=("Arial",20))
L1.grid(row=1, column=0, sticky="w")
L4 = Label(my_app, text="Bangun Persegi adalah salah satu bangun")
L4.grid(row=2, column=0, sticky="w")
L6 = Label(my_app, text="geometri 2 dimensi, dengan sisi yang sama")
L6.grid(row=3, column=0, sticky="w")
L3 = Label(my_app, text="Masukkan Sisi :")
L3.grid(row=4, column=0, sticky="w")
str1 = StringVar()
E3 = Entry(my_app, textvariable=str1)
E3.grid(row=4, column=1, sticky="w")

L2 = Button(my_app, text='Hitung luas', command=luas)
L2.grid(row=8, column=1, sticky="w")

L5 = Label(my_app)
L5.grid(row=8, column=2)
my_app.mainloop()
