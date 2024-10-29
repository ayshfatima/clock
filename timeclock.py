import tkinter as tk
from time import strftime
mnbx = tk.Tk()
mnbx.title("I show you time")
def date_time():
    string = strftime("%H:%M:%S %p \n %D") #%p for AM/PM
    label.config(text=string) # executes further code and displayes for label varibale
    label.after(1000,date_time) #shows live time changes when executed only once
label = tk.Label(mnbx,font=("calibri",50,"bold"),background="grey",foreground="white")
label.pack(anchor="center")
date_time()
mnbx.mainloop()




