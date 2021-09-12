from tkinter import *
from tkinter.ttk import *
from time import *
root = Tk()
root.title("Clock")
def time():
    string = strftime('%T:%M%p')
    #string = strftime('%d-%m-%Y %T:%M%p')
    label.config(text=string)
    label.after(1000,time)
label=Label(root, font=("ds_digital" , 20), background = "black", foreground = "cyan")
label.pack(anchor="center")
time()
mainloop()

