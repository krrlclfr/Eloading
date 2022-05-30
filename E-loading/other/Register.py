from tkinter import *
from tkinter import messagebox
import mysql.connector
import other

my_sql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dbShop"
    )

my_cursor = my_sql.cursor()

def back():
    roots.destroy()
    from other import Eloading
    Eloading.main()

def windows():
    roots.destroy()
    from other import Eloading
    Eloading.main()

def conn():

        
    dbname = name.get()
    dblastname = lastname.get()
    dbuser = user.get()
    dbpass = userpass.get()
    dbconfirm = ConfirmPass.get()
    dbgmail = usergmail.get()
    dbbal = 0
    dbpoints = 0

    if nameE == dbname and lastE == dblastname and usernameE == dbuser and passwordE == dbpass and gmail == dbgmail:
        message1 = messagebox.showinfo("Message", "Please dont leave it with blank ")

    elif nameE.get() == "" or lastE.get() == "" or usernameE.get() == "" or passwordE.get() == "" or gmail.get() == "":
        message2 = messagebox.showinfo("Message", "Please dont leave it with blank ")

    elif dbpass != dbconfirm :
        message3 = messagebox.showerror("Message", "Your password is not match ")
        
    else:   
       message4 = messagebox.showinfo("Message", "Thank you for registration , pleaselogin your account")
       insert = ("INSERT INTO tblaccount(Name, Lastname, Username, Password, Gmail, Balance, Points) Values(%s,%s,%s,%s,%s,%s,%s)")
       data = (dbname, dblastname, dbuser, dbpass, dbgmail, dbbal, dbpoints)
       my_cursor.execute(insert, data)
       my_sql.commit()
       windows()
    
    


#def confirm():
#    print(nameE.get())
#    print(lastE.get())
#    print(usernameE.get())
#    print(passwordE.get())
#    print(gmail.get())
#    
#    if nameE.get() == dbname and lastE.get() == dblastname and usernameE.get() == dbuser and passwordE.get() == dbpass and gmail.get() == dbgmail:
#        message2 = messagebox.showinfo("Message", "Thank you for registration , pleaselogin your account")
#        conn()
#    elif nameE.get() == "" or lastE.get() == "" or usernameE.get() == "" or passwordE.get() == "" or gmail.get() == "":
 #       message3 = messagebox.showinfo("Message", "Please dont leave it with blank ")
#    else:
#        message1 = messagebox.showinfo("Message", "Please dont leave it with blank ")

        
def enterback(event):
    backbtn.config(bg="#A6ACAF")
    backbtn.configure(bd=7)
    
def leftback(event):
    backbtn.config(bg="#D5D8DC")
    backbtn.configure(bd=5)

def entersubmit(event):
    SubmitButton.config(bg="#A6ACAF")
    SubmitButton.configure(bd=7)
    
def leftsubmit(event):
    SubmitButton.config(bg="#D5D8DC")
    SubmitButton.configure(bd=5)
    
def register():

    global roots
    global name
    global lastname
    global user
    global userpass
    global usergmail
    global ConfirmPass

    global nameE
    global lastE
    global passE
    global usernameE
    global passwordE
    global gmail
    
    global backbtn
    global SubmitButton
    roots = Tk()
    roots.title('Signup')
    roots.geometry("850x650+200+100")
    roots.configure(bg="#f0f0f0", pady=10)
    roots.resizable(0,0)
    frame = Frame(roots)
    frame.pack(side=TOP)

    name = StringVar()
    lastname = StringVar()
    user = StringVar()
    userpass = StringVar()
    ConfirmPass = StringVar()
    usergmail = StringVar()


    
    canvas = Label(roots, width=80, height=27, bg="#212F3D", relief=GROOVE, bd=5)
    canvas.place(x=45, y=100)
    
    intruction = Label(roots, text='Register account', relief=GROOVE, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white",bd=5) 
    intruction.pack()
    
    nameL = Label(roots, text='Name: ', bg="#212F3D", font='times 20 bold', fg="white")
    nameL.place(x=70, y=120)
    lastName = Label(roots, text='Last Name: ', bg="#212F3D", font='times 20 bold', fg="white")
    lastName.place(x=70, y=170)
    username = Label(roots, text='Username: ', bg="#212F3D", font='times 20 bold', fg="white")
    username.place(x=70, y=220)
    password = Label(roots, text='Password: ', bg="#212F3D", font='times 20 bold', fg="white")
    password.place(x=70, y=270)
    confirmL = Label(roots, text='Confirm Pass: ', bg="#212F3D", font='times 20 bold', fg="white")
    confirmL.place(x=70, y=320)
    GmailL = Label(roots, text='Gmail Account: ', bg="#212F3D", font='times 20 bold', fg="white")
    GmailL.place(x=70, y=370)
    
 
    nameE = Entry(roots, textvariable = name, width=15, font='times 20 bold', relief=GROOVE, bd=5)
    nameE.place(x=300, y=120)
    lastE = Entry(roots, textvariable =lastname, width=15, font='times 20 bold', relief=GROOVE, bd=5)
    lastE.place(x=300, y=170)
    usernameE = Entry(roots, textvariable = user, width=15, font='times 20 bold', relief=GROOVE, bd=5)
    usernameE.place(x=300, y=220)
    passwordE = Entry(roots, textvariable = userpass, width=15, font='times 20 bold', relief=GROOVE, bd=5, show = "*")
    passwordE.place(x=300, y=270)
    confirmpass = Entry(roots, textvariable = ConfirmPass, width=15, font='times 20 bold', relief=GROOVE, bd=5, show = "*")
    confirmpass.place(x=300, y=320)
    gmail = Entry(roots, textvariable = usergmail, width=21, font='times 15 bold', relief=GROOVE, bd=5)
    gmail.place(x=300, y=370)
    
    SubmitButton = Button(roots, text="Ok", bd=5, bg="#D5D8DC", font='times 10 bold', width=15, height=2, command=conn, cursor = "circle")
    SubmitButton.place(x=280, y=450)
    SubmitButton.bind("<Enter>", entersubmit)
    SubmitButton.bind("<Leave>", leftsubmit)

    backbtn = Button(roots, text = "Back", bd=5, bg="#D5D8DC", font='times 10 bold', width=8, command=back, cursor = "circle")
    backbtn.place(x=730, y=30)
    backbtn.bind("<Enter>", enterback)
    backbtn.bind("<Leave>", leftback)

    
    registerlogo = PhotoImage(file='icon\\register.png')
    logo = Label(roots, image=registerlogo)
    logo.place(x=620, y=180)
    roots.mainloop()

register() 
exit()
 
