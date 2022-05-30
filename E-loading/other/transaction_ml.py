from tkinter import *
import mysql.connector
import other
import random

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dbshop"
    )
my_cursor = mysql.cursor()

def bck():
    root.destroy()
    from other import product
    product.product_list(Uname)

    
    
def value():
    global pts
   
    
    ten = Label(root, textvariable = val, bg="#212F3D", font='times 20 bold', fg="white")
    ten.place(x=520, y=270)


    if val.get() == 10:
        pts = 1
        total_buy = Label(root, text = "+Points:     " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
    elif val.get() == 20:
        pts = 2
        total_buy = Label(root, text = "+Points:    " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=605, y=270)

    elif val.get() == 50:
        pts = 5
        total_buy = Label(root, text = "+Points:     " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    elif val.get() == 100:
        pts = 10
        total_buy = Label(root, text = "+Points:   " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    elif val.get() == 200:
        pts = 20
        total_buy = Label(root, text = "+Points:   " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    elif val.get() == 500:
        pts = 50
        total_buy = Label(root, text = "+Points:   " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    elif val.get() == 1000:
        pts = 150
        total_buy = Label(root, text = "+Points: " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    elif val.get() == 2000:
        pts = 300
        total_buy = Label(root, text = "+Points: " + str(pts), bg="#212F3D", font='times 20 bold', fg="white")
        total_buy.place(x=600, y=270)
        
    else:
        messagebox.showerror("Message", "Invalid")

def codes():

    global pas
    global pascode

    rand = random.randint(1,9)


    if rand == 1:
        pas = "CODE: AX98P23S"
        pascode = "PASSWORD: 99321AWDSDW"
    elif rand == 2:
        pas = "BSD87DSG"
        pascode = "PASSWORD: 19232ASWSFS"
    elif rand == 3:
        pas = "GEW32HRW"
        pascode = "PASSWORD: 757WQWW3245"
    elif rand == 4:
        pas = "547JHCSS"
        pascode = "PASSWORD: DSAXSWF7821"
    elif rand == 5:
        pas = "12DSAGD"
        pascode = "PASSWORD: LKIXNN67211"
    elif rand == 6:
        pas = "MBED21QQ"
        pascode = "PASSWORD: 896HSCBV54"
    elif rand == 7:
        pas = "ZXS76W3A"
        pascode = "PASSWORD: 097NBMXIHC"
    elif rand == 8:
        pas = "PAKN908S"
        pascode = "PASSWORD: 011100XCSCW"
    elif rand == 9:
        pas = "02SAQQ23"
        pascode = "PASSWORD: MIAKHALIFA123"
    else:
        print("12345")

def confrm():

    if val.get() == 0:
        messagebox.showerror("Message", "Please check ammount")
    elif val.get() > balnce:
        messagebox.showerror("Message", "Sorry insufficient balance")
    elif balnce == 0:
        messagebox.showerror("Message", "Not enough balance")
    else:
        send()
    
def send():
    
    answer = messagebox.askquestion("Message", "Are you sure to buy it?")
    if answer == "yes":
        codes()
        total = int(balnce - val.get())

        print(total)
        print("Congrats")
    
        messagebox.showinfo("Message", "Thank you have a nice day")

        update = ("UPDATE tblaccount SET Balance = '%s' WHERE Username = %s;")
        data = (total, Uname)
        my_cursor.execute(update, data)
        



        new_pts = user_points + pts
        print(new_pts)
        
  
        update_pts = ("UPDATE tblaccount SET Points = '%s' WHERE Username = %s;")
        up_pts = (new_pts, Uname)
        my_cursor.execute(update_pts, up_pts)
            
        mysql.commit()
                        
        root.destroy()
        textfile = open("Transaction.txt", "a")
        textfile.write("User: " + str(Uname))
        textfile.write("\n")
        textfile.write("Email: " + str(Emails.get()))
        textfile.write("\n")        
        textfile.write("Buy: " + str(val.get()))
        textfile.write("\n")
        textfile.write("Points: " + str(pts))
        textfile.write("\n")
        textfile.write("CODE: " + str(pas))
        textfile.write("\n")
        textfile.write("PASSCODE: " + str(pascode))
        textfile.write("\n")
        textfile.close()
        from other import user_window
        user_window.main(Uname)

        
        
    elif answer == "no":
        print("See you next time")
        
    else:
        print("Invalid")
        
        
        
    
def transact(User_name):

    global val
    global root
    global Uname
    global balnce
    global user_points
    global Emails
    print(User_name)

    Uname = User_name

    select = ("SELECT * from tblaccount WHERE username = '%s';"%User_name)
    my_cursor.execute(select)

    result = my_cursor.fetchall()

    for x in result:
        print(x)
        balnce = x[6]
        user_points = x[7]
    
    root = Tk()
    root.geometry("850x550+200+100")
    root.title("Transactions")
    root.configure()
    root.resizable(0, 0)

    frame = Frame(root, pady=20, bg="#A6ACAF")
    frame.pack(side=TOP)

    transac = Label(frame, text="Your transaction ", relief=GROOVE, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
    transac.pack()

    backbtn = Button(frame, text="Back", bd=5, bg="#D5D8DC", font='times 10 bold', width=8, command = bck)
    backbtn.place(x=750, y=30)

    val = IntVar()
    Emails = StringVar()
    
    ten = Label(root, text= "10 load", font='times 20 bold', bg="#212F3D", fg="white", width=12, height=1,relief=SUNKEN,bd=5)
    checkbtnten = Radiobutton(root, text="", bg="#212F3D", variable=val, value=10, command=value, activebackground="#212F3D")
    checkbtnten.place(x=40, y=150)
    ten.place(x=20, y=140)


    twenty = Label(root, text= "20 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN, bd=5)
    twenty.place(x=220, y=140)
    checkbtntwenty = Radiobutton(root, text="", bg="#212F3D", variable=val, value=20, command=value, activebackground="#212F3D")
    checkbtntwenty.place(x=240, y=150)

    sikwenta = Label(root, text= "50 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN,bd=5)
    sikwenta.place(x=420, y=140)
    checkbtnsikwenta = Radiobutton(root, text="", bg="#212F3D", variable=val, value=50, command=value, activebackground="#212F3D")
    checkbtnsikwenta.place(x=440, y=150)

    one_hundred = Label(root, text= "100 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN,bd=5)
    one_hundred.place(x=620, y=140)
    checkbtnonehundred = Radiobutton(root, text="", bg="#212F3D", variable=val, value=100, command=value, activebackground="#212F3D")
    checkbtnonehundred.place(x=640, y=150)

    two_hundred = Label(root, text= "200 load", font='times 20 bold', bg="#212F3D", fg="white", width=12, height=1,relief=SUNKEN,bd=5)
    two_hundred.place(x=20, y=190)
    checkbtntwohundred = Radiobutton(root, text="", bg="#212F3D", variable=val, value=200, command=value, activebackground="#212F3D")
    checkbtntwohundred.place(x=40, y=200)

    five_hundred = Label(root, text= "500 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN,bd=5)
    five_hundred.place(x=220, y=190)
    checkbtnfivehundred = Radiobutton(root, text="", bg="#212F3D", variable=val,  value=500, command=value, activebackground="#212F3D")
    checkbtnfivehundred.place(x=240, y=200)

    one_thousand = Label(root, text= "1000 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN, bd=5)
    one_thousand.place(x=420, y=190)
    checkbtnonethousand = Radiobutton(root, text="", bg="#212F3D", variable=val, value=1000, command=value, activebackground="#212F3D")
    checkbtnonethousand.place(x=440, y=200)

    two_thousand = Label(root, text= "2000 load", font='times 20 bold', bg="#212F3D", fg="white", width=12,relief=SUNKEN, bd=5)
    two_thousand.place(x=620, y=190)
    checkbtntwothousand = Radiobutton(root, text="", bg="#212F3D", variable=val, value=2000, command=value, activebackground="#212F3D")
    checkbtntwothousand.place(x=640, y=200)

    
    canvas = Label(root, text=" ", bg="#212F3D", width=113, height=10,relief=GROOVE, bd=5)
    canvas.place(x=20, y=240)

    bgcanvas = Label(root, text="",bg="#212F3D", width=70, height=8,relief=SUNKEN, bd=5)
    bgcanvas.place(x=300, y=255)

    buy = Label(root, text="Buy: ", bg="#212F3D", font='times 20 bold', fg="white")
    buy.place(x=350, y=270) 

    bal = Label(root, text="Balance:          " + str(balnce),bg="#212F3D", font='times 20 bold', fg="white")
    bal.place(x=350, y=320)
 
    canvas2 = Label(root, text=" ", bg="#212F3D", width=113, height=5,relief=GROOVE, bd=5)
    canvas2.place(x=20, y=410)
    email = Label(root, text="Email: ", bg="#212F3D", fg="white", font='times 20 bold', bd=5)
    email.place(x=50, y=440)
    emailEntry = Entry(root, textvariable=Emails, font='times 20 bold', width=25,relief=GROOVE)
    emailEntry.place(x=160, y=440)

    sendbtn = Button(root, text="Send", bg="#212F3D", fg="White", font='times 10 bold', width=10, height=2,relief=GROOVE, bd=5, activebackground="#A6ACAF", command = confrm)
    sendbtn.place(x=380, y=500)


    lol = PhotoImage(file='icon\\mlicon.png')
    lolicon = Button(root, image=lol, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
    lolicon.place(x=80, y=248)
    
    
    root.mainloop()



