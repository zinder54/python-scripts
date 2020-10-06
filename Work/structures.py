from tkinter import Tk, Button, Entry, Label, StringVar
from tkinter import *
import tkinter.ttk as ttk

app = Tk()
app.title("Kiwa site calculations")
app.resizable(0, 0)
app.geometry("750x300")

m1 = PanedWindow(orient = HORIZONTAL)
m1.grid(row=0, column=0, sticky ="nsew")
app.grid_rowconfigure(5, weight=5)
app.grid_columnconfigure(5, weight=5)
m2 = PanedWindow(m1, orient = HORIZONTAL)

scrollbar = Scrollbar(m1,  orient = HORIZONTAL, command=m1.yview)
L1 = Label(m1, text="Client",
           pady=15,
           padx=10).grid(row=0, column=1)
E1 = Entry(m1).grid(row=1, column=1)

L2 = Label(m1, text = "Site",
           pady=15,
           padx=30).grid(row=0, column=2)
E2 = Entry(m1).grid(row=1, column=2)

L3 = Label(m1, text="Location",
           pady=15,
           padx=30).grid(row = 0, column =3)
E3 = Entry(m1).grid(row=1, column=3)

L4 = Label(m1, text="Job REF.",
           pady=15,
           padx=30).grid(row=0, column=4)
E4 = Entry(m1).grid(row=1, column=4)

L5 = Label(m1, text="DATE",
           pady=15,
           padx=30).grid(row=0, column=5)
E5 = Entry(m1).grid(row=1, column=5)

L6 = Label(m1, text="Length under Test",
           pady=5,
           padx=0).grid(row=2,column=4)
E6 = Entry(m1).grid(row=2, column=5)

L7 = Label(m1, text="Spec. load/m(Bedding)",
           pady=5,
           padx=0).grid(row=2,column=3)

L7a = Label(m1, text="Kn/m",
           pady=0,
           padx=0).grid(row=3,column=2)
E7a = Entry(m1).grid(row=3, column=3)

L7b = Label(m1, text="/m",
           pady=0,
           padx=0).grid(row=4,column=2)
E7b = Entry(m1).grid(row=4, column=3)

L8 = Label(m1, text="Spec. load/m(Proof)",
            pady=0,
            padx=0).grid(row=2, column=1)
L8a = Label(m1, text="Kn/m",
            pady=0,
            padx=0).grid(row=3, column=0)
E8a = Entry(m1).grid(row=3, column=1)
L8b = Label(m1, text="/m",
            pady=0,
            padx=0).grid(row=4, column=0)
E8b = Entry(m1).grid(row=4, column=1)

L9 = Label(m1,text="Load at X(bedding)",
            pady=0,
            padx=0,).grid(row=3, column=4)
E9 = Entry(m1).grid(row=3,column=5)

L10 = Label(m1,text="Load at X(Proof)",
            pady=0,
            padx=0,).grid(row=4, column=4)
E10 = Entry(m1).grid(row=4,column=5)

LB1 = Label(m1, text="barrier,Span/",
            pady=0,
            padx=0).grid(row=5,column=0)
EB1 = Entry(m1).grid(row=5,column=1)
EB2 = Entry(m1).grid(row=5,column=2)
EB3 = Entry(m1).grid(row=5,column=3)
EB4 = Entry(m1).grid(row=5,column=4)
EB5 = Entry(m1).grid(row=5,column=5)

LB2 = Label(m1, text="Bedding load",
            pady=0, padx=0).grid(row=6,column=0)

#height  = 10
#width = 10
#for i in range(height):
 #   for j in range(width):
  #      tkinter.Entry(app, text= "comments").grid(row=2, column=2)

app.mainloop()
