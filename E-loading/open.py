from tkinter import messagebox

import os


def openfile():
    try:
       os_open = os.startfile('C:\\wamp64\\wampmanager.exe')

       if os_open is true:
           print("Hello")

       else:
           print("Error")
        
    except Exception as e:
            print(e)
 
            messagebox.showerror("Message", "Error")

openfile()
