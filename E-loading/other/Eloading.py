from tkinter import *
from ttkthemes import themed_tk as tk
from tkinter import messagebox
import other
import mysql.connector

my_sql = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "dbShop"
    )

my_cursor = my_sql.cursor()


my_cursor.execute('''CREATE TABLE IF NOT EXISTS tblaccount(
                  id int auto_increment not null,
                  Name varchar(255) not null,
                  Lastname varchar(255) not null,
                  Username varchar(255) not null,
                  Password varchar(255) not null,
                  Gmail varchar(255) not null,
                  Balance int(255) not null,
                  Points int(255) not null,
                  primary key(id));
                  ''')


    
class gui1():
    def __init__(self, root):
        self.topFrame = Frame(root, pady=20, bg="#A6ACAF")
        self.topFrame.pack(side=TOP)

        self.welcome = Label(self.topFrame, text="DDAJJ E-Loading shop",relief=SUNKEN, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
        self.welcome.pack()

        self.signupBtn = Button(self.topFrame, text="Login", bd=5, bg="#D5D8DC", font='times 10 bold', command=self.login)
        self.signupBtn.place(x=780, y=10)
        self.signupBtn.bind("<Enter>", self.entersignup)
        self.signupBtn.bind("<Leave>", self.leftsignup)
        
        self.registerBtn = Button(self.topFrame, text="Register", bd=5, bg="#D5D8DC", font='times 10 bold', command=self.regist)                
        self.registerBtn.place(x=710, y=10)
        self.registerBtn.bind("<Enter>", self.enterregister)
        self.registerBtn.bind("<Leave>", self.leftregister)
        
        self.lolphoto = PhotoImage(file='icon\\lol.png')
        self.lol = Button(root, image=self.lolphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=self.please)
        self.lol.place(x=15, y=150)
        self.lol.bind("<Enter>", self.enterlol)
        self.lol.bind("<Leave>", self.leftlol)
        
        self.mlphoto = PhotoImage(file='icon\\ml.png')
        self.ml = Button(root, image=self.mlphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=self.please)
        self.ml.place(x=570, y=120)
        self.ml.bind("<Enter>", self.enterml)
        self.ml.bind("<Leave>", self.leftml)
        
        self.pubgphoto = PhotoImage(file='icon\\pubg.png')
        self.pubg = Button(root, image=self.pubgphoto, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D", command=self.please)
        self.pubg.place(x=570, y=320)
        self.pubg.bind("<Enter>", self.enterpubg)
        self.pubg.bind("<Leave>", self.leftpubg)
        #################################################################################
        
        #plus more button into the next photo of the vouncher
        self.btnMore = Button(root, text="+ More", bd=10, bg="#D5D8DC", width= 20, font='times 10 bold', command=self.please)
        self.btnMore.place(x=350, y=500)
        self.btnMore.bind("<Enter>", self.entermore)
        self.btnMore.bind("<Leave>", self.leftmore)
        #################################################################################
    def backbtn(self):
        
        self.gameLoad.destroy()
        main()

        
    def nxt(self):
        
        root.destroy()
        global gameLoad
        self.gameLoad = Tk()
        self.gameLoad.geometry("850x550")
        self.gameLoad.configure(bg="#A6ACAF")
        self.gameLoad.resizable(0,0)
        
        self.TopFrame = Frame(self.gameLoad, pady=20, bg="#A6ACAF")
        self.TopFrame.pack(side=TOP)

        self.backbtn = Button(self.gameLoad, text="Back", bd=5, bg="#D5D8DC", font='times 10 bold', width=8, command=self.backbtn)
        self.backbtn.place(x=30, y=50)
        
        self.Choose = Label(self.TopFrame, text="Choose",relief=SUNKEN, bg="#212F3D", width=60,pady=20, font='times 30 bold', fg="white")
        self.Choose.pack()

        #first row for gameload
        self.lol = PhotoImage(file='icon\\lolicon.png')
        self.lolicon = Button(self.gameLoad, image=self.lol, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.lolicon.place(x=70, y=150)

        self.pubg = PhotoImage(file='icon\\pubgicon.png')
        self.pubgicon = Button(self.gameLoad, image=self.pubg, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.pubgicon.place(x=270, y=150)
        
        self.ml = PhotoImage(file='icon\\mlicon.png')
        self.mlicon = Button(self.gameLoad, image=self.ml, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.mlicon.place(x=470, y=150)

        self.ragnarok = PhotoImage(file='icon\\ragnarokicon.png')
        self.ragnarokicon = Button(self.gameLoad, image=self.ragnarok, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.ragnarokicon.place(x=670, y=150)
        ##########################################################################################

        
        #second row for gameload
        self.cod = PhotoImage(file='icon\\codicon.png')
        self.codicon = Button(self.gameLoad, image=self.cod, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.codicon.place(x=70, y=350)

        self.freefire = PhotoImage(file='icon\\freefireicon.png')
        self.freefireicon = Button(self.gameLoad, image=self.freefire, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.freefireicon.place(x=270, y=350)
        
        self.lordsmobile = PhotoImage(file='icon\\lordsmobileicon.png')
        self.lordsmobileicon = Button(self.gameLoad, image=self.lordsmobile, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.lordsmobileicon.place(x=470, y=350)

        self.laplacem = PhotoImage(file='icon\\laplacemicon.png')
        self.laplacemicon = Button(self.gameLoad, image=self.laplacem, relief=GROOVE, bd=9, bg="#17202A", activebackground="#7B7D7D")
        self.laplacemicon.place(x=670, y=350)
        ########################################################################################

        #Mouse event

    def login(self):
        root.destroy()
        root.quit()
        from other import SampleLogin
        SampleLogin.Signup()


    def regist(self):
        root.destroy()
        root.quit()
        from other import Register
        Register.register()

    def please(self):
        
        message = messagebox.showinfo("Message", "Please login first")

        
    def enterpubg(self, event):
        self.pubg.config(bg="#7B7D7D")
    def leftpubg(self,event):
        self.pubg.config(bg="#17202A")
    def enterlol(self,event):
        self.lol.config(bg="#7B7D7D")
    def leftlol(self,event):
        self.lol.config(bg="#17202A")
    def enterml(self,event):
        self.ml.config(bg="#7B7D7D")
    def leftml(self,event):
        self.ml.config(bg="#17202A")
    def entermore(self,event):
        self.btnMore.config(bg="white")
    def leftmore(self,event):
        self.btnMore.config(bg="#D5D8DC")
    def enterregister(self,event):
        self.registerBtn.config(bg="white")
    def leftregister(self,event):
        self.registerBtn.config(bg="#D5D8DC")
    def entersignup(self, event):
        self.signupBtn.config(bg="white")
    def leftsignup(self,event):
        self.signupBtn.config(bg="#D5D8DC")
###########################################
        
def main():
    global root
    root = Tk()
    root.title("DDAJJ E-Loading shop")
    root.configure(bg="#A6ACAF")
    root.geometry("850x550+200+100")
    root.resizable(0, 0)
    gui = gui1(root)
    root.mainloop()
main()

exit()


