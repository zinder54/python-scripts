import tkinter as tk
from tkinter import *
from tkinter import ttk

#create the gui app and size of the app
app = Tk()
nb = ttk.Notebook(app)

main_frame = Frame(nb) 
bedding_frame = Frame(main_frame,width=500,height=50,borderwidth=5, relief='flat')
proof1_frame = Frame(main_frame,width=500,height=50,borderwidth=5, relief='flat')
proof2_frame = Frame(main_frame,width=500,height=50,borderwidth=5, relief='flat')

bedding_frame.pack(side='top')
proof1_frame.pack(side='bottom')
proof2_frame.pack(side='bottom')
nb.add(main_frame, text="main")
nb.pack(pady=15)
app.grid_rowconfigure(6, weight=6)
app.grid_columnconfigure(6, weight=6)

L1= Label(bedding_frame, text="Span").grid(row=0)
L2 = Label(bedding_frame, text="Bedding Load").grid(row=1)

height = 7 
width = 6
for i in range(height): #Rows
    for j in range(width): #Columns
        if i == 2:
            continue
        bedding = Entry(bedding_frame)
        proof1 = Entry(proof1_frame)
        proof2 = Entry(proof2_frame)
        bedding.grid(row=i, column=1+j)
        proof1.grid(row=i, column=1+j)
        proof2.grid(row=i, column=1+j)

app.mainloop()
