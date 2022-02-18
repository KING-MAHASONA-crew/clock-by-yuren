# https://github.com/KING-MAHASONA-crew/

# Licened under GNU 3.0 or later.
# Don't try to fork or Replace it with your codes.
# Respect For the Devoloper.

# Coded by Yuren Sasanka.

from tkinter import *
from tkinter.ttk import *

from time import strftime

root =Tk()
root.title("Clock By Yuren Sasanka")


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("ds-digital", 80), background = "black", foreground= "cyan")
label.pack(anchor='center')
time()

mainloop()