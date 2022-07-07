from Tkinter import Tk, Label, Entry, Button
from tkMessageBox import showinfo

my_app = Tk(className='All About Me')
T = Label(my_app, text="Data diri", font=("Arial",24))
T.grid(row=0, column=0, sticky="w")
L1 = Label(my_app, text="Nama")
L1.grid(row=1, column=0, sticky="w")
E1 = Label(my_app, text="Irvan Rifa'i")
E1.grid(row=1, column=1, sticky="w")
L2 = Label(my_app, text="NIM")
L2.grid(row=2, column=0, sticky="w")
E2 = Label(my_app, text="L200180214")
E2.grid(row=2,column=1, sticky="w")
L3 = Label(my_app, text="Buku Favorit")
L3.grid(row=3, column=0, sticky="w")
E3 = Label(my_app, text="The Psychology of Money")
E3.grid(row=3,column=1, sticky="w")
L4 = Label(my_app, text="Idola dari kalangan sahabat")
L4.grid(row=4, column=0, sticky="w")
E4 = Label(my_app, text="Nabi Muhammad SAW")
E4.grid(row=4,column=1, sticky="w")
L5 = Label(my_app, text="Motto")
L5.grid(row=5, column=0, sticky="w")
E5 = Label(my_app, text="Berusaha jadi baik, juga bermanfaat")
E5.grid(row=5,column=1, sticky="w")

def tampil_pesan():
    my_app.destroy()

B = Button(my_app, text="Tutup", command=tampil_pesan)
B.grid(row=6, column=1)
my_app.mainloop()
