import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import os
from tkinter.ttk import *
from time import strftime

def execute_command():
    user_command = entry2.get()
    output = os.popen(user_command).read()

    txt.delete('1.0', 'end')
    txt.insert('1.0', output)

dracule = tk.Tk()
dracule.geometry('550x350')
dracule.title('cmd version=anime')
dracule.configure(background='#16141a')
dracule.resizable(False, False)


path = '././dbs10.png'

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(dracule, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

fontecust = font.Font(family="Courier", size=8)
fontecust2 = font.Font(family="Courier", size=13)
fontecust3 = font.Font(family="Courier", size=8)


button = tk.Button(highlightthickness=5, text='COMMAND', font=fontecust, height=1, cursor="hand2", command=execute_command, borderwidth=3)
button.config(highlightbackground="#180147", highlightcolor="#180147", background='black', foreground='#DF7CFA')
button.place(x=5, y=6)

entry2 = tk.Entry(dracule, width=41, borderwidth=7, background='black', foreground='#DF7CFA', font=fontecust2)
entry2.place(x=80, y=5)


txt = tk.Text(dracule, height=10, width=50, borderwidth=5, bg='black', foreground='pink')
txt.place(x=80, y=110)

coded = tk.Label(dracule, text='coded by YASHasvi', background='black', font=fontecust3, foreground='#DF7CFA', cursor='hand2')
coded.place(x=420, y=330)



dracule.mainloop()
