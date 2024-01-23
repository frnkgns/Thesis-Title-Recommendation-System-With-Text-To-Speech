import customtkinter
from customtkinter import *
from subprocess import call
from CTkMessagebox import *
import sqlite3
import pyttsx3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

MainWindow = CTk()

WindowWidth = 350
WindowHeight = 300

ScreenWidth = MainWindow.winfo_screenwidth()
ScreenHeight = MainWindow.winfo_screenheight()

x = (ScreenWidth / 2) - (WindowWidth / 2)
y = (ScreenHeight / 2) - (WindowHeight / 2)

MainWindow.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
MainWindow.resizable(False, False)
MainFrame = CTkFrame(MainWindow, height= 500, width= 350)
MainFrame.place(relx= 0, rely= 0)

ID = CTkEntry(MainFrame, width= 100, placeholder_text= "ID")
ID.place(relx= 0.35, rely= 0.2)
SignInBtn = CTkButton(MainFrame, text= "LOGIN", width= 100, command= lambda: RetrieveAccount())
SignInBtn.place(relx= 0.35, rely= 0.3)
SignUpBtn = CTkButton(MainFrame, text= "Not registered yet?", width= 60, fg_color= "transparent", hover_color= "#212121", command= lambda: OpenRegistrationForm())
SignUpBtn.place(relx= 0.33, rely= 0.38)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def OpenRegistrationForm():
    MainWindow.destroy()
    call(["python", "RegistrationForm.py"])
def ChangeButtonTextColor():
    SignUpBtn.configure(text_color= "#1F538D")
def ChangeButtonTextDefault():
    SignUpBtn.configure(text_color= "#FFFFFF")

SignUpBtn.bind("<Enter>", lambda change: ChangeButtonTextColor())
SignUpBtn.bind("<Leave>", lambda change: ChangeButtonTextDefault())

#-----------------------------------------------------------------------------------------
con = sqlite3.connect("Data.db")
cur = con.cursor()

def RetrieveAccount():
    global RetrievedId
    GetID = ID.get()

    query = f"""
        select id from accountinfo
        where id = '{GetID}'
    """

    cur.execute(query)
    try:
        RetrievedId = cur.fetchall()[0][0]
    except:
        RetrievedId = "asd"

    if len(GetID) == 0:
        engine.say("enter your id to continue")
        engine.runAndWait()

    else:
        if RetrievedId == GetID:
            with open("LogInID", "r+") as LogInID:
                Read = LogInID.readline()

                if Read:
                    LogInID.seek(0)
                    LogInID.truncate()
                    LogInID.write(RetrievedId)
                else:
                    LogInID.seek(0)
                    LogInID.write(RetrievedId)

            engine.say("id found, continue to login")
            engine.runAndWait()

            MainWindow.destroy()
            call(["python", "main.py"])

        else:
            engine.say("id is not registered yet, would you like to register?")
            engine.runAndWait()
            NoID = CTkMessagebox(title="No ID Found", message="ID not registered yet \nwould like to register?",
                                 icon="cancel", option_1="Yes")

            if NoID.get() == "Yes":
                OpenRegistrationForm()


MainWindow.bind("<Return>", lambda e: RetrieveAccount())
MainWindow.mainloop()
