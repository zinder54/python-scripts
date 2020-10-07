from tkinter import Tk, Button, Entry, Label, StringVar
from tkinter import *
import tkinter.ttk as ttk

app = Tk()
app.title("Kiwa site calculations")
app.resizable(1000, 1000)
app.geometry("710x500")

main_frame = Frame(app,width=500,height=50, borderwidth=5, relief='raised')
second_frame = Frame(app,width=500,height=50, borderwidth=5)
main_frame.grid(row=0, sticky ="w")
second_frame.grid(row=1, sticky ="w")
app.grid_rowconfigure(5, weight=5)
app.grid_columnconfigure(4, weight=5)

L1 = Label(main_frame, text="Client",
           pady=15,
           padx=10).grid(row=0, column=1)
E1 = Entry(main_frame).grid(row=1, column=1)

L2 = Label(main_frame, text = "Site",
           pady=15,
           padx=30).grid(row=0, column=2)
E2 = Entry(main_frame).grid(row=1, column=2)

L3 = Label(main_frame, text="Location",
           pady=15,
           padx=30).grid(row = 0, column =3)
E3 = Entry(main_frame).grid(row=1, column=3)

L4 = Label(main_frame, text="Job REF.",
           pady=15,
           padx=30).grid(row=0, column=4)
E4 = Entry(main_frame).grid(row=1, column=4)

L5 = Label(main_frame, text="DATE",
           pady=15,
           padx=30).grid(row=0, column=5)
E5 = Entry(main_frame).grid(row=1, column=5)

L6 = Label(main_frame, text="Length under Test",
           pady=5,
           padx=0).grid(row=2,column=4)
E6 = Entry(main_frame).grid(row=2, column=5)

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
E11 = Entry(main_frame).grid(row=5,column=1)
E12 = Entry(main_frame).grid(row=5,column=2)
E13 = Entry(main_frame).grid(row=5,column=3)
E14 = Entry(main_frame).grid(row=5,column=4)
E15 = Entry(main_frame).grid(row=5,column=5)

sfL1 = Label(second_frame, text="Bedding cycle",
            pady=0, padx=0).grid(row=0,column=0)
sfL2 = Label(second_frame, text="MAX DEF.",
            pady=0, padx=0).grid(row=1,column=0)
sfL3 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=2,column=0)
sfE1 = Entry(second_frame).grid(row=0,column=1)
sfE2 = Entry(second_frame).grid(row=0,column=2)
sfE3 = Entry(second_frame).grid(row=0,column=3)
sfE4 = Entry(second_frame).grid(row=0,column=4)
sfE5 = Entry(second_frame).grid(row=0,column=5)
sfE6 = Entry(second_frame).grid(row=1,column=1)
sfE7 = Entry(second_frame).grid(row=1,column=2)
sfE8 = Entry(second_frame).grid(row=1,column=3)
sfE9 = Entry(second_frame).grid(row=1,column=4)
sfE10 = Entry(second_frame).grid(row=1,column=5)
sfE11 = Entry(second_frame).grid(row=2,column=1)
sfE12 = Entry(second_frame).grid(row=2,column=2)
sfE13 = Entry(second_frame).grid(row=2,column=3)
sfE14 = Entry(second_frame).grid(row=2,column=4)
sfE15 = Entry(second_frame).grid(row=2,column=5)

sfL4 = Label(second_frame, text="Proof cycle",
            pady=5, padx=0).grid(row=3,column=0)
sfL5 = Label(second_frame, text="MAX DEF.",
            pady=0, padx=0).grid(row=4,column=0)
sfL6 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=5,column=0)
sfL7 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=5,column=0)
sfL8 = Label(second_frame, text="RESIDUAL DEF.",
            pady=0, padx=0).grid(row=5,column=0)

#height  = 10
#width = 10
#for i in range(height):
 #   for j in range(width):
  #      tkinter.Entry(app, text= "comments").grid(row=2, column=2)

app.mainloop()
