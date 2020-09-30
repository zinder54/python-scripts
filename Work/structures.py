from tkinter import Tk, Button, Entry, Label, StringVar
import tkinter.ttk as ttk

app = Tk()
app.title("Kiwa site calculations")
app.resizable(0, 0)
app.geometry("750x300")



L1 = Label(app, text="Client",
           pady=15,
           padx=10).grid(row=0, column=1)
E1 = Entry(app).grid(row=1, column=1)

L2 = Label(app, text = "Site",
           pady=15,
           padx=30).grid(row=0, column=2)
E2 = Entry(app).grid(row=1, column=2)

L3 = Label(app, text="Location",
           pady=15,
           padx=30).grid(row = 0, column =3)
E3 = Entry(app).grid(row=1, column=3)

L4 = Label(app, text="Job REF.",
           pady=15,
           padx=30).grid(row=0, column=4)
E4 = Entry(app).grid(row=1, column=4)

L5 = Label(app, text="DATE",
           pady=15,
           padx=30).grid(row=0, column=5)
E5 = Entry(app).grid(row=1, column=5)

L6 = Label(app, text="barrier REF. No.",
           pady=5,
           padx=0).grid(row=2,column=4)
E6 = Entry(app).grid(row=3, column=4)

L7 = Label(app, text="Spec. load/m(Bedding)",
           pady=5,
           padx=0).grid(row=2,column=3)

L7a = Label(app, text="Kn/m",
           pady=0,
           padx=0).grid(row=3,column=2)
E7a = Entry(app).grid(row=3, column=3)

L7b = Label(app, text="/m",
           pady=0,
           padx=0).grid(row=4,column=2)
E7b = Entry(app).grid(row=4, column=3)

L8 = Label(app, text="Spec. load/m(Proof)",
            pady=0,
            padx=0).grid(row=2, column=1)
L8a = Label(app, text="Kn/m",
            pady=0,
            padx=0).grid(row=3, column=0)
E8a = Entry(app).grid(row=3, column=1)
L8b = Label(app, text="/m",
            pady=0,
            padx=0).grid(row=4, column=0)
E8b = Entry(app).grid(row=4, column=1)

L9 = Label(app,text="Length under test",
            pady=0,
            padx=0,).grid(row=2, column=5)
E9 = Entry(app).grid(row=3,column=5)

LB1 = Label(app, text="Span/",
            pady=0,
            padx=0).grid(row=5,column=0)
EB1 = Entry(app).grid(row=5,column=1)
EB2 = Entry(app).grid(row=5,column=2)
EB3 = Entry(app).grid(row=5,column=3)
EB4 = Entry(app).grid(row=5,column=4)
EB5 = Entry(app).grid(row=5,column=5)

LB2 = Label(app, text="Bedding load",
            pady=0, padx=0).grid(row=6,column=0)

#height  = 10
#width = 10
#for i in range(height):
 #   for j in range(width):
  #      tkinter.Entry(app, text= "comments").grid(row=2, column=2)

app.mainloop()
