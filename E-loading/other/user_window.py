from tkinter import *
import mysql.connector
import other
global userName

mysql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dbshop"
    )

mycursor = mysql.cursor()



def add_acc():
    
    global tols
    global ammounts
    global acc
    
    master.destroy()
    
    total = IntVar()
    acc = str(accounts.get())
    try:
        ammounts = int(ammount.get())
        
        #Selecting data from tblbannkacc where bankaccountn
        sql = ("SELECT * FROM tblbannkacc WHERE bankaccount = '%s';"%acc)
    
        db = mycursor.execute(sql)
        result = mycursor.fetchall()

        #Print the data column index []
        for x in result:
            print(x[1])
            print(x[2])
            bal = x[2]

    
            
        if acc == x[1]:
            total = int(bal - ammounts)
            print(total)
            
            select = ("SELECT * FROM tblaccount WHERE username = '%s';"%userName)
            mycursor.execute(select)
            result1 = mycursor.fetchall()

            #print the data index
            for x in result1:
                print(x[6])
                balnce = int(x[6])


            
            try:
                if ammounts >= bal:
                    messagebox.showerror("Message", "Sorry insufficient balance in your bank account")
                   
                else:
                    tols = int(balnce + ammounts)
                    messagebox.showinfo("Message", "Thank you have a nice day")
                    #Update data

                    totals = ("UPDATE tblbannkacc SET Balance = '%s' WHERE bankaccount = %s;")
                    ups = (total, acc)
                    mycursor.execute(totals, ups)
    

        
                    up = ("UPDATE tblaccount SET Balance = '%s' WHERE Username = %s;")
                    gg = (tols, userName)
                    mycursor.execute(up, gg)
                    mysql.commit()
    
                    balance = Label(topFrame, text = "Balance: " + str(tols), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    
            except Exception as e:
                print(e)
                messagebox.showerror("Message", "Sorry not enough balance")
        
        elif acc != x[1]:
            messagebox.showerror("Message", "Invalid")
        
        else:
            messagebox.showerror("Message", "Invalid")
        
    except Exception as e:
            print(e)
            messagebox.showerror("Message", "Invalid bank account")       
 
    

def close(clo):

    if clo == 1:
        convert_win.destroy()
    elif clo == 2:        
        master.destroy()
    else:
        print("Error")

def converts_points():

    global total_bals
    con = messagebox.askquestion("Message", "Are you sure to convert it?")

    if con == "yes":
        try:
            if adds == 5:
                if pts >= val_con:
                    add_bal = bals + adds
                    print(add_bal)

                    total_bals = adds + bals
                    total_points = pts - val_con

                    ups_bal = ("UPDATE tblaccount SET Balance = %s WHERE Username = %s;")
                    ups_exe = (total_bals, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    balance = Label(topFrame, text="Balance: " + str(total_bals), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    print("Success")

                    
                    
                    ups_bal = ("UPDATE tblaccount SET Points = %s WHERE Username = %s;")
                    ups_exe = (total_points, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    points = Label(topFrame, text="Points:   "+ str(total_points), font='times 13 bold', fg="white", bg="#212F3D")
                    points.place(x=10, y=60)
                    
                    convert_win.destroy()
                    mysql.commit()
                else:
                    messagebox.showerror("Invalid", "Insufficient Points")
                
            elif adds == 10:
                if pts >= val_con:
                    add_bal = bals + adds
                    print(add_bal)

                    total_bals = adds + bals
                    total_points = pts - val_con

                    ups_bal = ("UPDATE tblaccount SET Balance = %s WHERE Username = %s;")
                    ups_exe = (total_bals, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    balance = Label(topFrame, text="Balance: " + str(total_bals), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    print("Success")

                    
                    
                    ups_bal = ("UPDATE tblaccount SET Points = %s WHERE Username = %s;")
                    ups_exe = (total_points, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    points = Label(topFrame, text="Points:   "+ str(total_points), font='times 13 bold', fg="white", bg="#212F3D")
                    points.place(x=10, y=60)
                    
                    convert_win.destroy()
                    mysql.commit()
                else:
                    messagebox.showerror("Invalid", "Insufficient Points")
            elif adds == 70:
                if pts >= val_con:
                    add_bal = bals + adds
                    print(add_bal)

                    total_bals = adds + bals
                    total_points = pts - val_con

                    ups_bal = ("UPDATE tblaccount SET Balance = %s WHERE Username = %s;")
                    ups_exe = (total_bals, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    balance = Label(topFrame, text="Balance: " + str(total_bals), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    print("Success")

                    
                    
                    ups_bal = ("UPDATE tblaccount SET Points = %s WHERE Username = %s;")
                    ups_exe = (total_points, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    points = Label(topFrame, text="Points:   "+ str(total_points), font='times 13 bold', fg="white", bg="#212F3D")
                    points.place(x=10, y=60)
                    
                    convert_win.destroy()
                    mysql.commit()
                else:
                    messagebox.showerror("Invalid", "Insufficient Points")
            elif adds == 100:
                if pts >= val_con:
                    add_bal = bals + adds
                    print(add_bal)

                    total_bals = adds + bals
                    total_points = pts - val_con

                    ups_bal = ("UPDATE tblaccount SET Balance = %s WHERE Username = %s;")
                    ups_exe = (total_bals, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    balance = Label(topFrame, text="Balance: " + str(total_bals), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    print("Success")

                    
                    
                    ups_bal = ("UPDATE tblaccount SET Points = %s WHERE Username = %s;")
                    ups_exe = (total_points, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    points = Label(topFrame, text="Points:   "+ str(total_points), font='times 13 bold', fg="white", bg="#212F3D")
                    points.place(x=10, y=60)
                    
                    convert_win.destroy()
                    mysql.commit()
                else:
                    messagebox.showerror("Invalid", "Insufficient Points")
            elif adds == 500:
                if pts >= val_con:
                    add_bal = bals + adds
                    print(add_bal)

                    total_bals = adds + bals
                    total_points = pts - val_con

                    ups_bal = ("UPDATE tblaccount SET Balance = %s WHERE Username = %s;")
                    ups_exe = (total_bals, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    balance = Label(topFrame, text="Balance: " + str(total_bals), font='times 13 bold', fg="white", bg="#212F3D")
                    balance.place(x=10, y=30)
                    print("Success")

                    
                    
                    ups_bal = ("UPDATE tblaccount SET Points = %s WHERE Username = %s;")
                    ups_exe = (total_points, userName)
                    mycursor.execute(ups_bal, ups_exe)
                    points = Label(topFrame, text="Points:   "+ str(total_points), font='times 13 bold', fg="white", bg="#212F3D")
                    points.place(x=10, y=60)
                    
                    convert_win.destroy()
                    mysql.commit()
                else:
                    messagebox.showerror("Invalid", "Insufficient Points")
            else:
                print("Invalid")
                convert_win.destroy()
                
        except Exception as e:
            messagebox.showerror("Message", "Thank you")
           
            
    elif con == "no":
         print("Okay lang")

    else:
         print("Invalid")

def value_convert():
    
    global adds
    global val_con
    convert_val = val_cons.get()
    
    if convert_val == 150:
        One_hundred = Label(convert_win, text="Add      5", font='times 15 bold', bg="#212F3D", fg="white")
        One_hundred.place(x=420, y=330)
        print("150")
        val_con = 150
        adds = 5
        print(adds)
        
    elif convert_val == 250:
        One_hundred = Label(convert_win, text="Add    10", font='times 15 bold', bg="#212F3D", fg="white")
        One_hundred.place(x=420, y=330)
        print("250")
        val_con = 250
        adds = 10
    elif convert_val == 500:
        One_hundred = Label(convert_win, text="Add    70", font='times 15 bold', bg="#212F3D", fg="white")
        One_hundred.place(x=420, y=330)
        print("500")
        adds = 70
        print(adds)
    elif convert_val == 1000:
        One_hundred = Label(convert_win, text="Add  100", font='times 15 bold', bg="#212F3D", fg="white")
        One_hundred.place(x=420, y=330)
        print("1000")
        val_con = 1000
        adds = 100
        print(adds)
    elif convert_val == 2000:
        One_hundred = Label(convert_win, text="Add  500", font='times 15 bold', bg="#212F3D", fg="white")
        One_hundred.place(x=420, y=330)
        print("2000")
        val_con = 2000
        adds = 500
        print(adds)
    else:
        print("Invalid")

    
def convert_btn():

    global val_cons
    global clo
    global convert_win
    convert_win = Toplevel()
    convert_win.configure(bg="#016878")
    convert_win.geometry('600x400+350+230')
    convert_win.overrideredirect(1)
    frame = Frame(convert_win,pady=10, padx=10,bg="#016878")
    frame.pack(side=TOP)
    
    add = Label(frame,text="Convert Points",relief=GROOVE, bg="#212F3D", width=23,pady=20, font='times 30 bold', fg="white")
    add.pack()

    val_cons = IntVar()
    clo = IntVar()
    bg=Label(convert_win,width=32,height=17,bg="#212F3D",relief=GROOVE)
    bg.place(x=75,y=120)
    bg1 = Label(convert_win,width=32,height=17,bg="#212F3D",relief=GROOVE)
    bg1.place(x=305,y=120)
#Points radiobutton left side
    points_label = Label(convert_win, text="Points", font='times 15 bold', width=10, relief = GROOVE)
    points_label.place(x=130, y=130)

    bal_label = Label(convert_win, text="Add to Balance", font='times 15 bold', width=15, relief = GROOVE)
    bal_label.place(x=330, y=130)

    
    One_hundred = Label(convert_win, text="150 Points             =", font='times 15 bold', bg="#212F3D", fg="white")
    One_hundred.place(x=120, y=170)
    r1 = Radiobutton(convert_win, text="", bg="#212F3D",variable = val_cons,  value=150, activebackground="#212F3D", command = value_convert)
    r1.place(x=80, y=172)

    Two_hundred = Label(convert_win, text="250 Points             =", font='times 15 bold', bg="#212F3D", fg="white")
    Two_hundred.place(x=120, y=200)
    r2 = Radiobutton(convert_win, text="", bg="#212F3D",variable = val_cons,  value=250, activebackground="#212F3D", command = value_convert)
    r2.place(x=80, y=202)

    Five_hundred = Label(convert_win, text="500 Points             =", font='times 15 bold', bg="#212F3D", fg="white")
    Five_hundred.place(x=120, y=230)
    r3 = Radiobutton(convert_win, text="", bg="#212F3D",variable = val_cons,  value=500, activebackground="#212F3D", command = value_convert)
    r3.place(x=80, y=232)

    One1_hundred = Label(convert_win, text="1000 Points           =", font='times 15 bold', bg="#212F3D", fg="white")
    One1_hundred.place(x=120, y=260)
    r4 = Radiobutton(convert_win, text="", bg="#212F3D",variable = val_cons,  value=1000, activebackground="#212F3D", command = value_convert)
    r4.place(x=80, y=262)

    Two2_hundred = Label(convert_win, text="2000 Points           =", font='times 15 bold', bg="#212F3D", fg="white")
    Two2_hundred.place(x=120, y=290)
    r5 = Radiobutton(convert_win, text="", bg="#212F3D",variable = val_cons,  value=2000, activebackground="#212F3D", command = value_convert)
    r5.place(x=80, y=292)
##########################################

#Add balance right side
    
    One_hundred = Label(convert_win, text="5 balance", font='times 15 bold', bg="#212F3D", fg="white")
    One_hundred.place(x=350, y=170)


    Two_hundred = Label(convert_win, text="20 balance", font='times 15 bold', bg="#212F3D", fg="white")
    Two_hundred.place(x=350, y=200)


    Five_hundred = Label(convert_win, text="70 balance", font='times 15 bold', bg="#212F3D", fg="white")
    Five_hundred.place(x=350, y=230)


    One1_hundred = Label(convert_win, text="100 balance", font='times 15 bold', bg="#212F3D", fg="white")
    One1_hundred.place(x=350, y=260)


    Two2_hundred = Label(convert_win, text="500 balance", font='times 15 bold', bg="#212F3D", fg="white")
    Two2_hundred.place(x=350, y=290)


    b = Button(convert_win, text="OK", bd=5, bg="#D5D8DC", font='times 10 bold', width=10, command = converts_points)
    b.place(x=200,y=330)
    b2 = Button(convert_win, text="CANCEL", bd=5, bg="#D5D8DC", font='times 10 bold', width=10, command =lambda:close(1))
    b2.place(x=320,y=330)
    convert.mainloop()
    
def add_btn():
    global master
    global accounts
    global ammount
    global account_entry
    global ammount_entry
    
    
    master = Toplevel()
    master.overrideredirect(1)
    
    master.configure(bg="#016878")
    master.geometry('600x400+350+230')

    lastname = StringVar()
    acc = StringVar()
    frame = Frame(master,pady=10, padx=10,bg="#016878")
    frame.pack(side=TOP)

    accounts = StringVar()
    ammount = StringVar()
    bg=Label(master,width=65,height=15,bg="#212F3D",relief=GROOVE)
    bg.place(x=70,y=120)

    add = Label(frame,text="Bank Account",relief=GROOVE, bg="#212F3D", width=23,pady=20, font='times 30 bold', fg="white")
    add.pack()

    account=Label(master, text = "Account number", bg="#212F3D", font='times 20 bold', fg="white")
    account.place(x=80,y=160)
    
    account_entry =  Entry(master, textvariable = accounts, fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    account_entry.place(x=285,y=160)
    
    gmail=Label(master, text = "Amount", bg="#212F3D", font='times 20 bold', fg="white")
    gmail.place(x=80,y=220)
    
    ammount_entry =  Entry(master, textvariable = ammount, fg="#212F3D", width=15, font='times 20 bold', relief=GROOVE, bd=9, bg="#A6ACAF")
    ammount_entry.place(x=285,y=220)

    b = Button(master, text="OK", bd=5, bg="#D5D8DC", font='times 10 bold', width=10, command = add_acc)
    b.place(x=200,y=300)
    b2 = Button(master, text="CANCEL", bd=5, bg="#D5D8DC", font='times 10 bold', width=10,command=lambda:close(2))
    b2.place(x=320,y=300)


def mlimg_btn():
    root.destroy()
    from other import transaction_ml
    transaction_ml.transact(userName)

def lolimg_btn():
    root.destroy()
    from other import transaction
    transaction.transact(userName)

def pubgimg_btn():
    root.destroy()
    from other import transaction_pubg
    transaction_pubg.transact(userName)

def lgout():
    root.destroy()
    from other import SampleLogin
    SampleLogin.Signup()


def load():
    root.destroy()
    from other import product
    product.product_list(userName)

    
def one(user_name_get):
    global userName
    print(user_name_get)

    userName = user_name_get
    main(userName)


#Mouse event
def enteredit(event):
    edit.config(bg="#7B7D7D", bd=2)
def leftedit(event):
    edit.config(bg="#212F3D", bd=1)

def enteradd(event):
    add.config(bg="#7B7D7D", bd=2)
def leftadd(event):
    add.config(bg="#212F3D", bd=1)

def enterconvert(event):
    convert.config(bg="#7B7D7D", bd=2)
def leftconvert(event):
    convert.config(bg="#212F3D", bd=1)

def enterlogout(event):
    logout.config(bg="#7B7D7D", bd=2)
def leftlogout(event):
    logout.config(bg="#212F3D", bd=1)

def enterpubg(event):
    pubg.config(bg="#7B7D7D")
def leftpubg(event):
    pubg.config(bg="#17202A")
def enterlol(event):
    lol.config(bg="#7B7D7D")
def leftlol(event):
    lol.config(bg="#17202A")
def enterml(event):
    ml.config(bg="#7B7D7D")
def leftml(event):
    ml.config(bg="#17202A")
def entermore(event):
    btnMore.config(bg="white")
def leftmore(event):
    btnMore.config(bg="#D5D8DC")
    
###########################################

#Start of main window
def main(userName):
    
    global lol
    global ml
    global btnMore
    global pubg
    global root
    global edit
    global add
    global convert
    global logout
    global topFrame
    global pts
    global bals

     
    select = ("SELECT * FROM tblaccount WHERE username = '%s';"%userName)
    mycursor.execute(select)
    result1 = mycursor.fetchall()

    for x in result1:
        print(x[6])
        print(x[7])
        bals = x[6]
        pts = x[7]

        
    root = Tk()
    root.title("DDAJJ E-Loading")
    root.configure(bg="#A6ACAF")
    root.geometry("850x550+200+100")
    root.resizable(0, 0)
    
#Top frame with sign up and register
    topFrame = Frame(root, pady=20, bg="#A6ACAF")
    topFrame.pack(side=TOP)

    welcome = Label(topFrame, text="DDAJJ E-Loading shop",relief=GROOVE, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
    welcome.pack()
    
    #display the who's user, how much balance and thier points

    
    user = Label(topFrame, text="User: " + userName, font='times 13 bold', fg="white", bg="#212F3D")
    user.place(x=10, y=5)
    
    balance = Label(topFrame, text="Balance: " + str(bals), font='times 13 bold', fg="white", bg="#212F3D")
    balance.place(x=10, y=30)

    points = Label(topFrame, text="Points: "+ str(pts), font='times 13 bold', fg="white", bg="#212F3D")
    points.place(x=10, y=60)


    #####################################################################################
    

    #Edit button, add balance, convert points and logout button side right
    edit = Button(topFrame, text="Edit", font='times 10 bold', fg="white", bg="#212F3D", relief= FLAT, bd=1, activeforeground="#212F3D")
    edit.place(x=650, y=10)
    edit.bind("<Enter>", enteredit)
    edit.bind("<Leave>", leftedit)

    add = Button(topFrame, text="Add", font='times 10 bold', fg="white", bg="#212F3D", relief= FLAT, activeforeground="#212F3D", bd=1,command=add_btn)
    add.place(x=690, y=10)
    add.bind("<Enter>", enteradd)
    add.bind("<Leave>", leftadd)    

    convert = Button(topFrame, text="Convert", font='times 10 bold', fg="white", bg="#212F3D", relief= FLAT, activeforeground="#212F3D", bd=1, command = convert_btn)
    convert.place(x=730, y=10)
    convert.bind("<Enter>", enterconvert)
    convert.bind("<Leave>", leftconvert)

    logout = Button(topFrame, text="Log out", font='times 10 bold', fg="white", bg="#212F3D", command=lgout, relief= FLAT, activeforeground="#212F3D", bd=1)
    logout.place(x=790, y=10)
    logout.bind("<Enter>", enterlogout)
    logout.bind("<Leave>", leftlogout)
    
    ######################################################################################

    
    #images for the game
    lolphoto = PhotoImage(file='icon\\lol.png')
    lol = Button(root, image=lolphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=lolimg_btn)
    lol.bind("<Enter>", enterlol)
    lol.bind("<Leave>", leftlol)
    lol.place(x=15, y=150)

    mlphoto = PhotoImage(file='icon\\ml.png')
    ml = Button(root, image=mlphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=mlimg_btn)
    ml.bind("<Enter>", enterml)
    ml.bind("<Leave>", leftml)
    ml.place(x=570, y=120)

    pubgphoto = PhotoImage(file='icon\\pubg.png')
    pubg = Button(root, image=pubgphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=pubgimg_btn)
    pubg.bind("<Enter>", enterpubg)
    pubg.bind("<Leave>", leftpubg)
    pubg.place(x=570, y=320)
    #################################################################################


    #plus more button into the next photo of the vouncher
    btnMore = Button(root, text="+ More", bd=10, bg="#D5D8DC", width= 20, font='times 10 bold', command=load)
    btnMore.place(x=350, y=500)
    btnMore.bind("<Enter>", entermore)
    btnMore.bind("<Leave>", leftmore)
    ##################################################################################



    root.mainloop()
    ##################################################################################
