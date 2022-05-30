from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import themed_tk as tk
import other
import mysql.connector


my_sql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    )

my_cursor = my_sql.cursor()


my_cursor.execute("CREATE DATABASE IF NOT EXISTS dbShop")
    
    

global root
root = tk.ThemedTk()
root.get_themes()
root.set_theme("alt")
root.geometry("320x40+500+350")
root.configure(bg="#A6ACAF")
root.overrideredirect(1)



progress = ttk.Progressbar(root, orient = HORIZONTAL, 
            length = 300, mode = 'determinate')

def dest():
    root.destroy()
    from other import Eloading
    Eloading.main()
    
def bar(): 
    import time
    progress['value'] = 20
    progress.update() 
    time.sleep(0.1) 
  
    progress['value'] = 40
    progress.update() 
    time.sleep(0.1) 
  
    progress['value'] = 50
    progress.update() 
    time.sleep(0.1) 
  
    progress['value'] = 60
    progress.update() 
    time.sleep(0.1) 
  
    progress['value'] = 80
    progress.update() 
    time.sleep(0.1)
    
    progress['value'] = 100
    progress.update()
    time.sleep(0.5)
    
    
    progress.stop()
    dest()


progress.pack(ipady =5, pady=6)
progress.start(bar())

root.mainloop()

