from tkinter import *
from tkinter import messagebox
import mysql.connector
import other
import random


def rand_pass():
     rand = random.randint(1,9)

     if rand == 1:
         pas = "AX98P23S"
     elif rand == 2:
         pas = "BSD87DSG"
     elif rand == 3:
         pas = "GEW32HRW"
     elif rand == 4:
         pas = "547JHCSS"
     elif rand == 5:
         pas = "12DSAGD"
     elif rand == 6:
         pas = "MBED21QQ"
     elif rand == 7:
         pas = "ZXS76W3A"
     elif rand == 8:
         pas = "PAKN908S"
     elif rand == 9:
         pas = "02SAQQ23"
     else:
         print("12345")
         
     name = user.get()

     select = ("SELECT * FROM tblaccount WHERE Username = '%s';"%name)
     my_cursor.execute(select)
     
     result = my_cursor.fetchall()

     for x in result:
         print(x[3])



     try:

         user_names = x[3]
         if name == user_names:
             messagebox.showinfo("Message", "You forgot your password, Check your current password in folder")
             textfile = open("Forget pass.txt", "a")

             textfile.write("Username: " + str(name))
             textfile.write("\n")
             textfile.write("Your new password: " + str(pas))
             textfile.write("\n")
             textfile.close()

             up = ("UPDATE tblaccount SET Password = %s WHERE Username = %s;")
             update_pass = (pas, name)
             my_cursor.execute(up, update_pass)
             my_sql.commit()
             
         else:
             messagebox.showerror("Message", "Invalid username")
             
     except Exception as e:
             messagebox.showerror("Message", "Sorry invalid username")
             forgetpass()





  

def close():
    forgets.destroy()

    
def forgetpass():
    global user
    global userEntry
    global forgets
    global send
    global cancel

    
    forgets = Toplevel()
    forgets.overrideredirect(1)
    forgets.title('Forget password')
    forgets.geometry('580x380+350+250')
    forgets.configure(bg="#016878")



    frame = Frame(forgets, pady=10, padx=15, bg="#016878")
    frame.pack(side=TOP)
    forgetpass = Label(frame, text='Forget Password\n',bg="#212F3D", width=23,pady=10, font='times 30 bold', fg="white", relief = GROOVE) 
    forgetpass.pack()
    
    bg=Label(forgets,width=65,height=12,bg="#212F3D",relief=GROOVE)
    bg.place(x=70,y=160)


    
    username = Label(forgets, text='Username ',bg="#212F3D", font='times 20 bold', fg="white")
    username.place(x=120,y=180)
    
    gmail = Label(forgets, text='Gmail ',bg="#212F3D", font='times 20 bold', fg="white")
    gmail.place(x=120,y=240)
    
    
    user = StringVar()
    
    userEntry = Entry(forgets,fg="#212F3D", textvariable = user, width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    userEntry.place(x=250,y=180)
    
    gmailEntry = Entry(forgets,fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    gmailEntry.place(x=250,y=240)

    send = Button(forgets,text="Send",bd=5, bg="#D5D8DC", font='times 10 bold', width=10,command= rand_pass)
    send.place(x=200,y=300)
    send.bind("<Enter>", entersend)
    send.bind("<Leave>", leftsend)
    
    cancel = Button(forgets,text="Cancel",bd=5, bg="#D5D8DC", font='times 10 bold', width=10,command= close)
    cancel.place(x=320,y=300)
    cancel.bind("<Enter>", entercancel)
    cancel.bind("<Leave>", leftcancel)
    
    #nameE.grid(row=1, column=1) 
    #pwordE.grid(row=2, column=1) 
 
    #signupButton = Button(roots, text='Signup')
    #signupButton.grid(columnspan=2, sticky=W)
    forgets.mainloop()


my_sql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dbshop"
    )

my_cursor = my_sql.cursor()


def back():
    
    roots.destroy()
    from other import Eloading
    Eloading.main()
    exit()
    
def userWindow():
    
    roots.destroy()
    from other import user_window
    user_window.one(user_name_get)
    
    
def confirm():
    global user_name_get
    user_name_get = str(user_name.get())
    user_pass_get = str(user_pass.get())

    print(user_name_get)
    
    user_sql = ("SELECT * FROM tblaccount WHERE username = '%s';"%user_name_get)
 


    exe = my_cursor.execute(user_sql)
    result = my_cursor.fetchall()
    print(result)

    for x in result:
        print(x[3].lower())
     
    for y in result:
        print(y[4])
        
    try:
        if user_name_get == x[3] and user_pass_get == y[4]:
            message1 = messagebox.showinfo("Message", "Thank you for your login please wait")
            userWindow()            
            
        else:
            message2 = messagebox.showinfo("Message", "Incorrect username or password")

    except Exception as e:
            print(e)
            print(user_name_get, user_pass_get)
            message2 = messagebox.showinfo("Message", "Invalid username and password")


    my_sql.commit()



def entercancel(event):
    cancel.config(bg="#A6ACAF")
    cancel.configure(bd=7)
    
def leftcancel(event):
    cancel.config(bg="#D5D8DC")
    cancel.configure(bd=5)
    
def entersend(event):
    send.config(bg="#A6ACAF")
    send.configure(bd=7)
    
def leftsend(event):
    send.config(bg="#D5D8DC")
    send.configure(bd=5)

    
def enterlogin(event):
    signupButton.config(bg="#A6ACAF")
    signupButton.configure(bd=7)
    
def leftlogin(event):
    signupButton.config(bg="#D5D8DC")
    signupButton.configure(bd=5)

def enterforget(event):
    forgetBtn.config(bg="#A6ACAF")
    forgetBtn.configure(bd=7)
    
def leftforget(event):
    forgetBtn.config(bg="#D5D8DC")
    forgetBtn.configure(bd=5)

def enterback(event):
    btnback.config(bg="#A6ACAF")
    btnback.configure(bd=7)
    
def leftback(event):
    btnback.config(bg="#D5D8DC")
    btnback.configure(bd=5)
    
 
def Signup():
    global roots
    global signupButton
    global forgetBtn
    global btnback

    global user_name
    global user_pass
    global nameE
    global pwordE
    
    roots = Tk() 
    roots.title('Login')
    roots.configure(bg="#A6ACAF")
    roots.geometry("950x650+200+100")
    roots.resizable(0, 0)
    frame1 = Frame(roots, pady=10)
    frame1.pack(side=TOP)

    bgLabel = Label(roots, width=105, heigh=25, bg="#212F3D", relief=GROOVE, bd=5)
    bgLabel.place(x=60, y=130)
    
    imglogo = PhotoImage(file='icon\\Login.png')
    loginLogo = Label(roots, image=imglogo, bg="#A6ACAF", relief=FLAT, bd=3)
    loginLogo.place(x=490, y=150)
    
    btnback = Button(roots, text="Back", bd=5, bg="#D5D8DC", font='times 10 bold', width=8, command=back, cursor = "circle")
    btnback.place(x=850, y=40)
    btnback.bind("<Enter>", enterback)
    btnback.bind("<Leave>", leftback)
    
    intruction = Label(frame1, text='Login your account',relief=SUNKEN, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
    intruction.pack(side=TOP) 
    nameL = Label(roots, text='Username: ', bg="#212F3D", font='times 20 bold', fg="white") 
    pwordL = Label(roots, text='Password: ', bg="#212F3D", font='times 20 bold', fg="white") 
    nameL.place(x=200, y=260) 
    pwordL.place(x=200, y=330)

    user_name = StringVar()
    user_pass = StringVar()
 
    nameE = Entry(roots, textvariable = user_name, fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    nameE.place(x=410, y=250)
    pwordE = Entry(roots, show='*', textvariable = user_pass, fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")  
    pwordE.place(x=410, y=320) 
 
    signupButton = Button(roots, text='Log in', bd=5, bg="#D5D8DC", font='times 10 bold', width=15, command = confirm, cursor="circle") 
    signupButton.place(x=380, y=400)
    signupButton.bind("<Enter>", enterlogin)
    signupButton.bind("<Leave>", leftlogin)

    forgetBtn = Button(roots, text='Forget you password?', bd=5, bg="#D5D8DC", font='times 10 bold', cursor = "circle",command=forgetpass) 
    forgetBtn.place(x=540, y=400)
    forgetBtn.bind("<Enter>", enterforget)
    forgetBtn.bind("<Leave>", leftforget)
    roots.mainloop()

Signup()
exit()
