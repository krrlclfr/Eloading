from tkinter import *
import random
import other
import mysql.connector

mysql = mysql.connector.connect(
     host = "localhost",
     user = "root",
     passwd = "",
     database = "dbshop"
     )
my_cursor = mysql.cursor()

def rand_pass():

     name = user.get()

     select = ("SELECT * FROM tblaccount WHERE Username = '%s';"%name)
     select1 = ("SELECT * FROM tblaccount WHERE Username = '%s';"%userEntry.get())
     my_cursor.execute(select, select1)
     
     result = my_cursor.fetchall()

     for x in result:
          print(x)
          
     print (random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9))

def close():
    roots.destroy()
 

 
def Forget(): 
    
    global roots
    global user
    global userEntry
    
    roots = Tk()
    roots.overrideredirect(1)
    roots.title('Signup')
    roots.geometry('580x380+350+250')
    roots.configure(bg="#A6ACAF")



    frame = Frame(roots, pady=10)
    frame.pack(side=TOP)
    forgetpass = Label(frame, text='Forget Password\n',bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white") 
    forgetpass.pack()
    
    bg=Label(roots,width=65,height=12,bg="#212F3D",relief=GROOVE)
    bg.place(x=70,y=160)


    
    username = Label(roots, text='Username ',bg="#212F3D", font='times 20 bold', fg="white")
    username.place(x=120,y=180)
    
    gmail = Label(roots, text='Gmail ',bg="#212F3D", font='times 20 bold', fg="white")
    gmail.place(x=120,y=240)
    
    
    user = StringVar()
    
    userEntry = Entry(roots,fg="#212F3D", textvariable = user, width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    userEntry.place(x=250,y=180)
    
    gmailEntry = Entry(roots,fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    gmailEntry.place(x=250,y=240)

    send=Button(roots,text="Send",bd=5, bg="#D5D8DC", font='times 10 bold', width=10,command= rand_pass)
    send.place(x=200,y=300)
    send=Button(roots,text="Cancel",bd=5, bg="#D5D8DC", font='times 10 bold', width=10,command= close)
    send.place(x=320,y=300)
    
    #nameE.grid(row=1, column=1) 
    #pwordE.grid(row=2, column=1) 
 
    #signupButton = Button(roots, text='Signup')
    #signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()


