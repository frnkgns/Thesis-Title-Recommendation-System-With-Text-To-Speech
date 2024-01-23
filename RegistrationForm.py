import customtkinter
from customtkinter import *
import sqlite3
from subprocess import call
from CTkMessagebox import  CTkMessagebox
import pyttsx3

MainWindow = CTk()
WindowWidth = 500
WindowHeight = 400

ScreenWidth = MainWindow.winfo_screenwidth()
ScreenHeight = MainWindow.winfo_screenheight()

x = (ScreenWidth / 2) - (WindowWidth / 2)
y = (ScreenHeight / 2) - (WindowHeight / 2)

MainWindow.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
MainWindow.resizable(False, False)

Mainframe = CTkFrame(MainWindow, height=WindowHeight, width=WindowWidth)
Mainframe.place(relx=0, rely=0)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voices = engine.getProperty('voices', )

#you need to put something inside the function if you where
#using the command= for combobox to avodi error
def ChangeFieldChoices(e):
    print("click")
    GetCourse = Course.get()

    if GetCourse == "BSCS":
        Field.configure(values= Cs)
    elif GetCourse == "BSIT":
        Field.configure(values= It)
    else:
        Field.configure(values= Emc)

def DisableRadioButtons(Type, Value):
    global Gender, Year

    if Type == "Year":
        if Value == 1:
            if Year1.get():
                Year = ""
                Year2.configure(state= "disabled")
                Year3.configure(state= "disabled")
                Year4.configure(state= "disabled")
            else:
                Year = ""
                Year2.configure(state="normal")
                Year3.configure(state="normal")
                Year4.configure(state="normal")
        elif Value == 2:
            if Year2.get():
                Year = "2"
                Year1.configure(state="disabled")
                Year3.configure(state="disabled")
                Year4.configure(state="disabled")
            else:
                Year = ""
                Year1.configure(state="normal")
                Year3.configure(state="normal")
                Year4.configure(state="normal")
        elif Value == 3:
            if Year3.get():
                Year = "3"
                Year1.configure(state="disabled")
                Year2.configure(state="disabled")
                Year4.configure(state="disabled")
            else:
                Year = ""
                Year1.configure(state="normal")
                Year2.configure(state="normal")
                Year4.configure(state="normal")
        else:
            if Year4.get():
                Year = "4"
                Year1.configure(state="disabled")
                Year2.configure(state="disabled")
                Year3.configure(state="disabled")
            else:
                Year = ""
                Year1.configure(state="normal")
                Year2.configure(state="normal")
                Year3.configure(state="normal")
    elif Type == "Gender":
        if Value == 1:
            if Male.get():
                Female.configure(state= "disabled")
                Gender = "Male"
            else:
                Female.configure(state= "normal")
                Gender = ""
        else:
            if Female.get():
                Male.configure(state= "disabled")
                Gender = "Female"
            else:
                Male.configure(state= "normal")
                Gender = ""

CreatingText = CTkLabel(Mainframe, font=(" ", 20), text="Creating Your \nAccount", justify= "left")
CreatingText.place(relx=0.05, rely=0.04)
Id = CTkEntry(Mainframe, placeholder_text="Student ID")
Id.place(relx=0.05, rely=0.2)
Fname = CTkEntry(Mainframe, placeholder_text="First Name")
Fname.place(relx=0.05, rely=0.3)
Lname = CTkEntry(Mainframe, placeholder_text="Last Name")
Lname.place(relx=0.05, rely=0.4)
Male = CTkCheckBox(Mainframe, text= "Male", command= lambda: DisableRadioButtons("Gender", 1))
Male.place(relx=0.05, rely=0.5)
Female = CTkCheckBox(Mainframe, text= "Female", command= lambda: DisableRadioButtons("Gender", 0))
Female.place(relx=0.2, rely=0.5)
CourseText = customtkinter.StringVar(value="Select Course")
Course = CTkComboBox(Mainframe, values=["BSCS", "BSIT", "BSEMC"], variable=CourseText, command= ChangeFieldChoices)
Course.place(relx=0.05, rely=0.6)

Year1 = CTkCheckBox(Mainframe, text= "1st", command= lambda: DisableRadioButtons("Year", 1))
Year1.place(relx=0.05, rely=0.7)
Year2 = CTkCheckBox(Mainframe, text= "2nd", command= lambda: DisableRadioButtons("Year", 2))
Year2.place(relx=0.2, rely=0.7)
Year3 = CTkCheckBox(Mainframe, text= "3rd", command= lambda: DisableRadioButtons("Year", 3))
Year3.place(relx=0.35, rely=0.7)
Year4 = CTkCheckBox(Mainframe, text= "4th", command= lambda: DisableRadioButtons("Year", 4))
Year4.place(relx=0.5, rely=0.7)

Cs = ["Data Mining", "Business Analytics"]
It = ["Web and Mobile App Development", "Network Security", "Business Process Outsourcing"]
Emc = ["Digital Art", "Game Development"]
FieldText = customtkinter.StringVar(value="Field")
Field = CTkComboBox(Mainframe, width=250, variable=FieldText, values= None)
Field.place(relx=0.05, rely=0.8)

#-----------Elements for LikesFrame inside MainFrame
LikesFrame = CTkScrollableFrame(Mainframe, label_text= "SELECT CATEGORY YOU LIKE",
                               label_font=("Consolas", 20, "bold"), width= 280,
                                label_fg_color= "transparent")
LikesFrame.place(relx= 0.35, rely= 0.05)
Categories = [
    "Agriculture, ",
    "Analytics, ",
    "Artificial Intelligence, ",
    "Automation, ",
    "Business, ",
    "Counseling, ",
    "Data Analysis, ",
    "E-Commerce, ",
    "Education, ",
    "Entertainment, ",
    "Financial Management, ",
    "Financial Monitoring, ",
    "Geographic Information System (GIS), ",
    "Healthcare, ",
    "Image Processing, ",
    "IOT (Internet of Things), ",
    "Inventory, ",
    "Lan-Based, ",
    "Law Enforcement, ",
    "Management System, ",
    "Mobile App Development, ",
    "Record Management, ",
    "Renewable Energy, ",
    "Scheduling System, ",
    "Security, ",
    "Social Services, ",
    "Student Services, ",
    "Transportation, ",
    "Tracking System, ",
    "Utilities, ",
    "Web-Based, "
]

def AppendSelectedCategory():
    for Category in Categories:
        if Likes[Category].get():
           Liked.append(Category)

    SavedData()


def DestroyThisForm():
    engine.say("Account creation complete, login to continue")
    engine.runAndWait()

    MainWindow.destroy()
    call(["python", "LogInForm.py"])

def SavedData():
    # accountinfo table structure
    # 0- id  2- firstname  3- lastname 4-gender    5- course   6-year  7- field    8-likes
    #variables
    try:
        GetID = Id.get()
        GetFname = Fname.get()
        GetLname = Lname.get()
        GetGender = Gender
        GetCourse = Course.get()
        GetYear = Year
        GetField = Field.get()
        GetLikes = "".join(map(str, Liked))

        con = sqlite3.connect('Data.db')
        cur = con.cursor()

        Insert = f"""
                insert into accountinfo values(
                '{GetID}', '{GetFname}',
                '{GetLname}', '{GetGender}',
                '{GetCourse}','{GetYear}',
                '{GetField}', '{GetLikes}')
            """

        cur.execute(Insert)
        con.commit()

        Insert = f"""
                    insert into accountstatistics values('{GetID}', 0, 0,'{GetLikes}')
                """

        cur.execute(Insert)
        con.commit()

        DestroyThisForm()

    except:
        engine.say("please fill up all the information")
        engine.runAndWait()



Liked = []
Likes = {}
index = 0
for Category in Categories:
    Likes[Category] = CTkCheckBox(LikesFrame, text= Category)
    Likes[Category].grid(column= 0, row= index, pady= 5, sticky= "w")

    index += 1

def GoBackToLogIn():
    MainWindow.destroy()
    call(["python", "LogInForm.py"])

GoBack = CTkButton(Mainframe, text= "Cancel", width= 80 ,command= lambda: GoBackToLogIn())
GoBack.place(relx= 0.6, rely= 0.8)
RegisterBtn = CTkButton(Mainframe, text= "Register", width= 80 ,command= lambda: AppendSelectedCategory())
RegisterBtn.place(relx= 0.8, rely= 0.8)

MainWindow.bind("<Return>", lambda e: SavedData())
MainWindow.mainloop()
