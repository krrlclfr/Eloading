from tkinter import *
import other
import mysql.connector

mysql = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "dbshop"
        )

my_cursor = mysql.cursor()
      
def buy_lol():
        
        gameLoad.destroy()
        from other import transaction
        transaction.transact(User_name)

def buy_pubg():
        gameLoad.destroy()
        from other import transaction_pubg
        transaction_pubg.transact(User_name)
        
def buy_ml():
        gameLoad.destroy()
        from other import transaction_ml
        transaction_ml.transact(User_name)

def buy_ragna():
        gameLoad.destroy()
        from other import transaction_ragna
        transaction_ragna.transact(User_name)

def buy_cod():
        gameLoad.destroy()
        from other import transaction_cod
        transaction_cod.transact(User_name)

def buy_ff():
        gameLoad.destroy()
        from other import transaction_ff
        transaction_ff.transact(User_name)

def buy_lords():
        gameLoad.destroy()
        from other import transaction_lords
        transaction_lords.transact(User_name)

def buy_laplace():
        gameLoad.destroy()
        from other import transaction_laplace
        transaction_laplace.transact(User_name)


def back():
        gameLoad.destroy()
        from other import user_window
        user_window.main(User_name)




#Mouse event everytime the cursor of the mouse enter and leave in icon
def enterpubg(event):
        pubgicon.config(bg="#7B7D7D", bd=12)
def leftpubg(event):
        pubgicon.config(bg="#17202A", bd=9)
def enterml(event):
        mlicon.config(bg="#7B7D7D", bd=12)
def leftml(event):
        mlicon.config(bg="#17202A", bd=9)
def enterlol(event):
        lolicon.config(bg="#7B7D7D", bd=12)
def leftlol(event):
        lolicon.config(bg="#17202A", bd=9)
def enterragnarok(event):
        ragnarokicon.config(bg="#7B7D7D", bd=12)
def leftragnarok(event):
        ragnarokicon.config(bg="#17202A", bd=9)
def entercod(event):
        codicon.config(bg="#7B7D7D", bd=12)
def leftcod(event):
        codicon.config(bg="#17202A", bd=9)
def enterlaplace(event):
        laplacemicon.config(bg="#7B7D7D", bd=12)
def leftlaplace(event):
        laplacemicon.config(bg="#17202A", bd=9)
def enterlm(event):
        lordsmobileicon.config(bg="#7B7D7D", bd=12)
def leftlm(event):
        lordsmobileicon.config(bg="#17202A", bd=9)
def enterff(event):
        freefireicon.config(bg="#7B7D7D", bd=12)
def leftff(event):
        freefireicon.config(bg="#17202A", bd=9)
##########################################################################

def product_list(userName):
    global pubgicon
    global mlicon
    global lolicon
    global freefireicon
    global ragnarokicon
    global codicon
    global laplacemicon
    global lordsmobileicon
    global gameLoad
    global User_name
    gameLoad = Tk()
    gameLoad.geometry("850x550+200+100")
    gameLoad.title("Product")
    gameLoad.configure(bg="#A6ACAF")
    gameLoad.resizable(0,0)
        
    TopFrame = Frame(gameLoad, pady=20, bg="#A6ACAF")
    TopFrame.pack(side=TOP)
    
    User_name = userName


    select = ("SELECT * FROM tblaccount WHERE username = '%s';"%User_name)
    my_cursor.execute(select)

    result = my_cursor.fetchall()

    for x in result:
        print(x)
        
        bal = x[6]
        pts = x[7]
    
    
    backbtn = Button(gameLoad, text="Back", bd=5, bg="#D5D8DC", font='times 10 bold', width=8, command=back)
    backbtn.place(x=730, y=50)

    user = Label(gameLoad, text="User: " + userName, font='times 13 bold', fg="white", bg="#212F3D")
    user.place(x=10, y=25)
    
    balance = Label(gameLoad, text="Balance: " + str(bal), font='times 13 bold', fg="white", bg="#212F3D")
    balance.place(x=10, y=50)

    points = Label(gameLoad, text="Points: " + str(pts), font='times 13 bold', fg="white", bg="#212F3D")
    points.place(x=10, y=75)
        
    Choose = Label(TopFrame, text="Choose",relief=GROOVE, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
    Choose.pack()

    #Box color for all the icon 
    canvas = Label(gameLoad, text="", width=115, height=26, relief=GROOVE, bd=5, bg="#212F3D")
    canvas.place(x=20, y=120)

    #first row for gameload
    lol = PhotoImage(file='icon\\lolicon.png')
    lolicon = Button(gameLoad, image=lol, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=buy_lol)
    lolicon.place(x=50, y=150)
    lolicon.bind("<Enter>", enterlol)
    lolicon.bind("<Leave>", leftlol)

    pubg = PhotoImage(file='icon\\pubgicon.png')
    pubgicon = Button(gameLoad, image=pubg, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=buy_pubg)
    pubgicon.place(x=270, y=150)
    pubgicon.bind("<Enter>", enterpubg)
    pubgicon.bind("<Leave>", leftpubg)
        
    ml = PhotoImage(file='icon\\mlicon.png')
    mlicon = Button(gameLoad, image=ml, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_ml)
    mlicon.place(x=470, y=150)
    mlicon.bind("<Enter>", enterml)
    mlicon.bind("<Leave>", leftml)

    ragnarok = PhotoImage(file='icon\\ragnarokicon.png')
    ragnarokicon = Button(gameLoad, image=ragnarok, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_ragna)
    ragnarokicon.place(x=670, y=150)
    ragnarokicon.bind("<Enter>", enterragnarok)
    ragnarokicon.bind("<Leave>", leftragnarok)
    ##########################################################################################

        
    #second row for gameload
    cod = PhotoImage(file='icon\\codicon.png')
    codicon = Button(gameLoad, image=cod, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_cod)
    codicon.place(x=50, y=350)
    codicon.bind("<Enter>", entercod)
    codicon.bind("<Leave>", leftcod)

    freefire = PhotoImage(file='icon\\freefireicon.png')
    freefireicon = Button(gameLoad, image=freefire, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_ff)
    freefireicon.place(x=270, y=350)
    freefireicon.bind("<Enter>", enterff)
    freefireicon.bind("<Leave>", leftff)
        
    lordsmobile = PhotoImage(file='icon\\lordsmobileicon.png')
    lordsmobileicon = Button(gameLoad, image=lordsmobile, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_lords)
    lordsmobileicon.place(x=470, y=350)
    lordsmobileicon.bind("<Enter>", enterlm)
    lordsmobileicon.bind("<Leave>", leftlm)

    laplacem = PhotoImage(file='icon\\laplacemicon.png')
    laplacemicon = Button(gameLoad, image=laplacem, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command = buy_laplace)
    laplacemicon.place(x=670, y=350)
    laplacemicon.bind("<Enter>", enterlaplace)
    laplacemicon.bind("<Leave>", leftlaplace)

    gameLoad.mainloop()
    #########################################################################################################

