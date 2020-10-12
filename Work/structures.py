from tkinter import Tk, Button, Entry, Label, StringVar
from tkinter import *
import tkinter.ttk as ttk

app = Tk()
app.title("Kiwa site calculations")
app.resizable(1000, 1000)
app.geometry("835x500")
nb = ttk.Notebook(app)



main_frame = ttk.Frame(nb,width=500,height=50,borderwidth=5, relief='raised')
second_frame = ttk.Frame(nb,width=500,height=50, borderwidth=1)
nb.add(main_frame, text="main")
nb.add(second_frame, text="second")
nb.select(main_frame)
nb.grid(app,row=1)
main_frame.grid(row=0, sticky ="w")
second_frame.grid(row=1, sticky ="w")
app.grid_rowconfigure(6, weight=6)
app.grid_columnconfigure(6, weight=6)


L1 = Label(main_frame, text="Client",
           pady=15,
           padx=10).grid(row=0, column=1)
for i in range(5):
    Entry(main_frame).grid(row=1, column=1+i)
L2 = Label(main_frame, text = "Site",
           pady=15,
           padx=30).grid(row=0, column=2)

L3 = Label(main_frame, text="Location",
           pady=15,
           padx=30).grid(row = 0, column =3)

L4 = Label(main_frame, text="Job REF.",
           pady=15,
           padx=30).grid(row=0, column=4)

L5 = Label(main_frame, text="DATE",
           pady=15,
           padx=30).grid(row=0, column=5)

L6 = Label(main_frame, text="Length under Test",
           pady=5,
           padx=0).grid(row=2,column=4)

L7 = Label(main_frame, text="Spec. load/m(Bedding)",
           pady=5,
           padx=0).grid(row=2,column=3)

L7a = Label(main_frame, text="Kn/m",
           pady=0,
           padx=0).grid(row=3,column=2)
E7a = Entry(main_frame).grid(row=3, column=3)

L7b = Label(main_frame, text="/m",
           pady=0,
           padx=0).grid(row=4,column=2)
E7b = Entry(main_frame).grid(row=4, column=3)

L8 = Label(main_frame, text="Spec. load/m(Proof)",
            pady=0,
            padx=0).grid(row=2, column=1)
L8a = Label(main_frame, text="Kn/m",
            pady=0,
            padx=0).grid(row=3, column=0)
E8a = Entry(main_frame).grid(row=3, column=1)
L8b = Label(main_frame, text="/m",
            pady=0,
            padx=0).grid(row=4, column=0)
E8b = Entry(main_frame).grid(row=4, column=1)

L9 = Label(main_frame,text="Load at X(bedding)",
            pady=0,
            padx=0,).grid(row=3, column=4)
E9 = Entry(main_frame).grid(row=3,column=5)

L10 = Label(main_frame,text="Load at X(Proof)",
            pady=0,
            padx=0,).grid(row=4, column=4)
E10 = Entry(main_frame).grid(row=4,column=5)

L11 = Label(main_frame, text="barrier, Span/ ",
            pady=0,
            padx=0).grid(row=5,column=0)
for i in range(6):
    Entry(main_frame).grid(row=5, column=1+i)

sfL1 = Label(second_frame, text="Bedding cycle",
            pady=0, padx=0).grid(row=0,column=0)
sfL2 = Label(second_frame, text="MAX DEF.",
            pady=0, padx=0).grid(row=1,column=0)
sfL3 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=2,column=0)
#For loop for full line entry boxes in second Frame
for i in range(6):
    Entry(second_frame).grid(row=0, column=1+i)
    Entry(second_frame).grid(row=1, column=1+i)
    Entry(second_frame).grid(row=2, column=1+i)
    Entry(second_frame).grid(row=4, column=1+i)
    Entry(second_frame).grid(row=5, column=1+i)
    Entry(second_frame).grid(row=6, column=1+i)
    Entry(second_frame).grid(row=7, column=1+i)

sfL4 = Label(second_frame, text="Proof cycle",
            pady=2, padx=0).grid(row=3,column=0)
sfL5 = Label(second_frame, text="MAX DEF.",
            pady=0, padx=0).grid(row=4,column=0)
sfL6 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=5,column=0)
sfL7 = Label(second_frame, text="RECOVERY",
            pady=0, padx=0).grid(row=6,column=0)
sfL8 = Label(second_frame, text="RECOVERY %",
            pady=0, padx=0).grid(row=7,column=0)
for i in range(5):
    Entry(second_frame).grid(row=4, column=1+i)
    Entry(second_frame).grid(row=2, column=1+i)


#height  = 10
#width = 10
#for i in range(height):
 #   for j in range(width):
  #      tkinter.Entry(app, text= "comments").grid(row=2, column=2)

app.mainloop()
