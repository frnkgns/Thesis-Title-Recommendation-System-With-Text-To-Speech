import customtkinter
from customtkinter import *
import sqlite3
from PIL import Image
from subprocess import call
import pyttsx3

AttributeClicked = 0
con = sqlite3.connect("Data.db")
cur = con.cursor()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
voices = engine.getProperty('voices', )

MainWindow = CTk()
TitleID = [
    "21-1",
    "22-2",
    "22-1",
    "22-2",
    "22-3",
    "22-4",
    "22-5",
    "22-6",
    "22-7",
    "22-8",
    "22-9",
    "22-10",
    "22-11",
    "22-12",
    "22-13",
    "22-7",
    "23-1",
    "23-2",
    "23-3",
    "23-4",
    "23-5",
    "23-6",
    "23-7",
    "23-8",
    "23-9",
    "23-10",
    "23-11",
    "23-12",
    "23-13",
    "23-14",
    "23-15",
    "23-16",
    "23-17",
    "23-18",
    "23-19",
    "23-20",
    "23-21",
    "23-22",
    "23-23",
    "23-24",
    "23-25",
    "23-26",
    "23-27",
    "23-28",
    "23-29",
    "23-30",
    "23-31",
    "23-32",
    "23-33",
    "23-34",
    "23-35",
    "23-36",
    "23-37",
    "23-38",
    "23-39",
    "23-40",
    "23-41",
    "23-42",
    "23-43",
    "23-44",
    "23-45",
    "23-46",
    "23-47",
    "23-48",
    "23-49",
    "23-50",
    "23-51",
    "23-52",
    "23-53",
    "23-54",
    "23-55",
    "23-56",
    "23-57",
    "23-58",
    "23-59",
    "23-60",
    "23-61",
    "23-62",
    "23-63",
    "23-64",
    "23-65",
    "23-66",
    "23-67",
    "23-68",
    "23-69",
    "23-70",
    "23-71",
    "23-72",
    "23-73",
]
Categories = [
    "Agriculture ",
    "Analytics ",
    "Artificial Intelligence ",
    "Automation ",
    "Business ",
    "Counseling ",
    "Data Analysis ",
    "E-Commerce ",
    "Education ",
    "Entertainment ",
    "Financial Management ",
    "Financial Monitoring ",
    "Geographic Information System (GIS) ",
    "Healthcare ",
    "Image Processing ",
    "IOT (Internet of Things) ",
    "Inventory ",
    "Lan-Based ",
    "Law Enforcement ",
    "Management System ",
    "Mobile App Development ",
    "Record Management ",
    "Renewable Energy ",
    "Scheduling System ",
    "Security ",
    "Social Services ",
    "Student Services ",
    "Transportation ",
    "Tracking System ",
    "Utilities ",
    "Web-Based "
]
Technologies = [
    "ajax",
    "android studio",
    "arduino",
    "arduino ide",
    "bootstrap",
    "c#",
    "c++",
    "codeigniter4",
    "css",
    "css3",
    "favicon",
    "gis",
    "html",
    "html5",
    "java",
    "javascript",
    "jquery",
    "kotlin",
    "mariadb",
    "mysql",
    "perl",
    "php",
    "python",
    "sublime text",
    "tomcat",
    "visual basic",
    "vs code",
    "xamp",
    "xml",
]
Year = ["2021", "2022", "2023"]

WindowWidth = 1000
WindowHeight = 500

ScreenWidth = MainWindow.winfo_screenwidth()
ScreenHeight = MainWindow.winfo_screenheight()

x = (ScreenWidth / 2) - (WindowWidth / 2)
y = (ScreenHeight / 2) - (WindowHeight / 2)

# MainWindow.geometry(f'{WindowWidth}x{WindowHeight}+{int(x)}+{int(y)}')
MainWindow.attributes("-fullscreen", True)

ProfileFrame = CTkFrame(MainWindow, height=300, width=200)
ProfileFrame.place(relx=0.01, rely=0.02)
StatisticFrame = CTkFrame(MainWindow, height=500, width=200)
StatisticFrame.place(relx=0.01, rely=0.42)


def ShowAllByYear(e):
    AllBooks("Year")
    ChoseByCategoryText = customtkinter.StringVar(value="Category")
    ChoseByCategory.configure(variable=ChoseByCategoryText)
    ChoseByTechnologiesText = customtkinter.StringVar(value="Technology")
    ChoseByTechnologies.configure(variable=ChoseByTechnologiesText)


def ShowAllByCategory(e):
    AllBooks("Category")
    ChoseByYearText = customtkinter.StringVar(value="Year")
    ChoseByYear.configure(variable=ChoseByYearText)
    ChoseByTechnologiesText = customtkinter.StringVar(value="Technology")
    ChoseByTechnologies.configure(variable=ChoseByTechnologiesText)


def ShowAllByTechnologies(e):
    AllBooks("Technologies")
    ChoseByYearText = customtkinter.StringVar(value="Year")
    ChoseByYear.configure(variable=ChoseByYearText)
    ChoseByCategoryText = customtkinter.StringVar(value="Category")
    ChoseByCategory.configure(variable=ChoseByCategoryText)


def GoBackToLogIn():
    MainWindow.destroy()
    call(["python", "LogInForm.py"])


Searchbar = CTkEntry(MainWindow, placeholder_text="Seach Title", width=530)
Searchbar.place(relx=0.165, rely=0.02)
ChoseByYearText = customtkinter.StringVar(value="Year")
ChoseByYear = CTkOptionMenu(MainWindow, values=Year, variable=ChoseByYearText,
                            dynamic_resizing=False, command=ShowAllByYear)
ChoseByYear.place(relx=0.558, rely=0.02)
ChoseByCategoryText = customtkinter.StringVar(value="Category")
ChoseByCategory = CTkOptionMenu(MainWindow, values=Categories, variable=ChoseByCategoryText,
                                command=ShowAllByCategory)
ChoseByCategory.place(relx=0.668, rely=0.02)

ChoseByTechnologiesText = customtkinter.StringVar(value="Technology")
ChoseByTechnologies = CTkOptionMenu(MainWindow, values=Technologies, variable=ChoseByTechnologiesText,
                                    command=ShowAllByTechnologies)
ChoseByTechnologies.place(relx=0.78, rely=0.02)

MultiPurposeBtn = CTkButton(MainWindow, text="Exit", fg_color="red", hover_color="darkred",
                            command=lambda: GoBackToLogIn())
MultiPurposeBtn.place(relx=0.89, rely=0.02)

# -------------Student Account------------------------------------------------
with open("LogInID", "r+") as LogInID:
    GetLoginID = LogInID.readline()


def RetrievedPersonalData():
    query = f"""
        select * from accountinfo
        where id = '{GetLoginID}'
    """
    cur.execute(query)
    Accountinfo = cur.fetchall()
    Accountinfolist = [e for e in Accountinfo]
    AccountInfo = ["ID", "First", "Last", "Gender", "Course", "Year", "Likes"]
    accountinfo = {}

    ID = Accountinfolist[0][0]
    Name = "Name: " + Accountinfolist[0][1] + " " + Accountinfolist[0][2]
    Gender = "Gender: " + Accountinfolist[0][3]
    Course = "Course: " + Accountinfolist[0][4] + "-" + str(Accountinfolist[0][5]) + ": " + Accountinfolist[0][6]
    Category = "Likes: " + Accountinfolist[0][7]

    DisplayID = CTkLabel(ProfileFrame, font=("", 20), text=ID)
    DisplayID.place(relx=0.3, rely=0.05)
    DisplayName = CTkLabel(ProfileFrame, text=Name, justify="left", wraplength=150)
    DisplayName.place(relx=0.1, rely=0.2)
    DisplayGender = CTkLabel(ProfileFrame, text=Gender, justify="left", wraplength=150)
    DisplayGender.place(relx=0.1, rely=0.35)
    DisplayCourse = CTkLabel(ProfileFrame, text=Course, justify="left", wraplength=150)
    DisplayCourse.place(relx=0.1, rely=0.5)
    DisplayCategory = CTkLabel(ProfileFrame, text=Category, justify="left", wraplength=150)
    DisplayCategory.place(relx=0.1, rely=0.7)


def AllBooks(Mode):
    global query, titles
    ExistedTitleFrame = {}
    ExistedTitleLabel = {}
    index = 0
    row = 0
    column = 0
    FirstRun = True

    ExistedTitleFrame.clear()
    ExistedTitleLabel.clear()
    RecommendedBookFrame = CTkScrollableFrame(MainWindow, height=300, width=750,
                                              label_text="ALL BOOKS",
                                              label_font=("Consolas", 30, "bold"),
                                              label_fg_color="transparent",
                                              label_anchor="w")
    RecommendedBookFrame.place(relx=0.165, rely=0.54)
    BookCover = CTkImage(light_image=Image.open("Book Front Cover.png"),
                         dark_image=Image.open("Book Front Cover.png"),
                         size=(165, 300))

    FrameHasElements = RecommendedBookFrame.winfo_children()
    if FrameHasElements:
        for elements in RecommendedBookFrame.winfo_children():
            elements.destroy()

    if Mode == "All":
        query = f"""
                    select * from bookinfo
                """
    elif Mode == "Year":
        SelectedYear = ChoseByYear.get()
        RecommendedBookFrame.configure(label_text=f"ALL BOOKS YEAR {SelectedYear.upper()}")
        FirstRun = False
        query = f"""
                    select * from bookinfo 
                    where year = '{SelectedYear}'
                """
    elif Mode == "Category":
        SelectedCategory = ChoseByCategory.get()
        selectedcategory = SelectedCategory.strip()
        RecommendedBookFrame.configure(label_text=f"ALL TITLES IN {selectedcategory.upper()} CATEGORY")
        FirstRun = False
        query = f"""
                    select * from bookinfo
                    where category like '%{selectedcategory}%'
                """
    elif Mode == "Technologies":
        SelectedTechnologies = ChoseByTechnologies.get()
        RecommendedBookFrame.configure(label_text=f"ALL TITLES THAT USES {SelectedTechnologies.upper()}")
        FirstRun = False
        query = f"""
                    select * from bookinfo
                    where technologies like '%{SelectedTechnologies}%'
                """
    elif Mode == "Search":
        SelectTitle = Searchbar.get()
        FirstRun = False
        if len(SelectTitle) >= 1:
            RecommendedBookFrame.configure(label_text=f"ALL TITLES THAT MATCHES {SelectTitle.upper()}")
            query = f"""
                    select * from bookinfo
                    where Titles like '%{SelectTitle}%'
                    """
        else:
            engine.say("you haven't entered something, search titles to continue")
            engine.runAndWait()
            AllBooks("All")
            # Reload the feed again to its user's recomendation

    cur.execute(query)
    TitleInfo = cur.fetchall()
    TitleInfolist = [e for e in TitleInfo]

    if len(TitleInfolist) > 0:
        for Title in TitleInfolist:
            titles = TitleInfolist[index][2]
            BookID = TitleInfolist[index][0]

            if column != 4:
                ExistedTitleFrame[Title] = CTkFrame(RecommendedBookFrame, height=285, width=150, fg_color="transparent")
                ExistedTitleFrame[Title].grid(column=column, row=row, padx=20, pady=10, sticky="w")
                ExistedTitleLabel[Title] = CTkLabel(ExistedTitleFrame[Title],
                                                    font=("Times New Roman", 14),
                                                    text=titles,
                                                    image=BookCover,
                                                    wraplength=100)
                ExistedTitleLabel[Title].place(relx=-0.02, rely=-0.02)
                ExistedTitleLabel[Title].bind("<Button-1>",
                                              lambda e, bookid=BookID, TiTles=titles:
                                              ShowBookInfo(bookid, TiTles))

                column += 1
            else:
                row += 1
                column = 0

                ExistedTitleFrame[Title] = CTkFrame(RecommendedBookFrame, height=285, width=150, fg_color="transparent")
                ExistedTitleFrame[Title].grid(column=column, row=row, padx=20, pady=10, sticky="w")
                ExistedTitleLabel[Title] = CTkLabel(ExistedTitleFrame[Title],
                                                    font=("Times New Roman", 14),
                                                    text=titles,
                                                    image=BookCover,
                                                    wraplength=100)
                ExistedTitleLabel[Title].place(relx=-0.02, rely=-0.02)
                ExistedTitleLabel[Title].bind("<Button-1>",
                                              lambda e, bookid=BookID, TiTles=titles:
                                              ShowBookInfo(bookid, TiTles))
                column += 1
            index += 1
    else:
        FirstRun = True
        engine.say("We don't have data yet that matches your preference")
        engine.runAndWait()
        AllBooks("All")

    EngineSays(FirstRun, index, Mode)


def EngineSays(FirstRun, numberoftitles, Mode):
    if FirstRun == True:
        pass
    else:
        if Mode == "Year":
            engine.say("I found " + str(numberoftitles) + " titles year " + ChoseByYear.get())
        elif Mode == "Category":
            engine.say("I found " + str(numberoftitles) + ChoseByCategory.get() + " titles ")
        elif Mode == "Technologies":
            engine.say("I found " + str(numberoftitles) + " that uses " + ChoseByTechnologies.get())
        elif Mode == "Search":
            if len(Searchbar.get()) > 1:
                engine.say("I found " + str(numberoftitles) + " that matches " + Searchbar.get())

        engine.runAndWait()


def ShowBookInfo(BookID, Booktitle):

    if len(BookID) > 1:
        engine.say(" Opening title id " + BookID)
        engine.runAndWait()
    else:
        engine.say(" Opening title ")
        engine.runAndWait()

    ChoseByYear.configure(state='disabled')
    ChoseByCategory.configure(state='disabled')
    ChoseByTechnologies.configure(state='disabled')

    titlecollectionframe = CTkFrame(MainWindow, height=720, width=775)
    titlecollectionframe.place(relx=0.165, rely=0.07)
    BookCover = CTkImage(light_image=Image.open("Book Front Cover.png"),
                         dark_image=Image.open("Book Front Cover.png"),
                         size=(365, 600))
    BookLabel = CTkLabel(titlecollectionframe, font=("Times New Roman", 25),
                         text=Booktitle, image=BookCover, wraplength=200)
    BookLabel.place(relx=0.05, rely=0.1)

    Hidebtn = CTkButton(titlecollectionframe, text="BACK", command=lambda: EnableSelection())
    Hidebtn.place(relx=0.75, rely=0.88)

    FrameHasElements = titlecollectionframe.winfo_children()
    if FrameHasElements:
        for widget in titlecollectionframe.winfo_children():
            widget.destroy

    query = f"""
                    select * from bookinfo
                    where titles = '{Booktitle}'
                """
    cur.execute(query)
    BookInfo = cur.fetchall()
    bookinfolist = [e for e in BookInfo]

    print(bookinfolist)
    ID = CTkLabel(titlecollectionframe, text="Title ID: " + str(bookinfolist[0][0]),
                  font=("Consolas", 20), justify="left", wraplength=300)
    ID.place(relx=0.55, rely=0.2)
    course = CTkLabel(titlecollectionframe, text="Course: " + str(bookinfolist[0][5]),
                      font=("Consolas", 20), justify="left", wraplength=300)
    course.place(relx=0.55, rely=0.25)
    year = CTkLabel(titlecollectionframe, text="Year Published: " + str(bookinfolist[0][1]),
                    font=("Consolas", 20), justify="left", wraplength=300)
    year.place(relx=0.55, rely=0.3)
    category = CTkLabel(titlecollectionframe, text="Category: " + str(bookinfolist[0][3]),
                        font=("Consolas", 20), justify="left", wraplength=300)
    category.place(relx=0.55, rely=0.35)
    technology = CTkLabel(titlecollectionframe, text="Technology Use: " + str(bookinfolist[0][4]),
                          font=("Consolas", 20), justify="left", wraplength=300)
    technology.place(relx=0.55, rely=0.43)
    location = CTkLabel(titlecollectionframe, text="Location: " + str(bookinfolist[0][6]),
                        font=("Consolas", 20), justify="left", wraplength=300)
    location.place(relx=0.55, rely=0.51)
    authors = CTkLabel(titlecollectionframe, text="Authors: " + str(bookinfolist[0][7]),
                       font=("Consolas", 20), justify="left", wraplength=300)
    authors.place(relx=0.55, rely=0.61)

    def EnableSelection():
        titlecollectionframe.destroy()
        ChoseByYear.configure(state='normal')
        ChoseByCategory.configure(state='normal')
        ChoseByTechnologies.configure(state='normal')

    query = f"""
        select nobookviewed, recentlyviewed from accountstatistics
        where id = '{GetLoginID}'
    """
    cur.execute(query)
    Accountinfo = cur.fetchall()
    accountinfolist = [e for e in Accountinfo]
    noofbookviewed = accountinfolist[0][0]
    recentlyviewed = bookinfolist[0][2]

    addviewbooks = noofbookviewed + 1

    query = f"""
        update accountstatistics
        set nobookviewed = '{addviewbooks}', recentlyviewed = '{recentlyviewed}'
        where id = '{GetLoginID}'
    """
    cur.execute(query)
    con.commit()

    query = f"""
        select noofviews from bookinfo
    """
    cur.execute(query)
    Noofviews = cur.fetchall()[0][0]
    newviews = int(Noofviews) + 1

    query = f"""
        update bookinfo
        set noofviews = '{newviews}'
        where "title id" = '{BookID}'
    """
    cur.execute(query)
    con.commit()

    MostViedBooks()
    ShoRecentViewed()

def ShoRecentViewed():
    global Booktitle
    RecentlyViewed = {}

    query = f"""
        select recentlyviewed from accountstatistics
        where id = '{GetLoginID}'
    """
    cur.execute(query)
    Booktitle = cur.fetchall()[0][0]

    FrameLabel = CTkLabel(StatisticFrame, text= "RECENTLY VIEWED", font= ("Consolas", 20, "bold"))
    FrameLabel.place(relx= 0.1, rely= 0.05)
    BookCover = CTkImage(light_image=Image.open("Book Front Cover.png"),
                         dark_image=Image.open("Book Front Cover.png"),
                         size=(165, 300))
    BookLabel = CTkLabel(StatisticFrame, font=("Times New Roman", 15),
                         text= Booktitle, image=BookCover, wraplength=100)
    BookLabel.place(relx=0.1, rely=0.15)
    BookLabel.bind("<Button-1>", lambda e, bookid= None, booktitle= Booktitle: ShowBookInfo(bookid, booktitle))
def MostViedBooks():
    global query, titles
    ExistedTitleFrame = {}
    ExistedTitleLabel = {}
    ExistedTitleLabels = {}
    index = 0
    row = 0
    column = 0

    RecommendedBookFrame = CTkScrollableFrame(MainWindow, height=650, width=330,
                                              label_text="TRENDING TITLES",
                                              label_font=("Consolas", 30, "bold"),
                                              label_fg_color="transparent",
                                              label_anchor="w")
    RecommendedBookFrame.place(relx=0.735, rely=0.07)
    BookCover = CTkImage(light_image=Image.open("Book Front Cover.png"),
                         dark_image=Image.open("Book Front Cover.png"),
                         size=(165, 300))
    FrameHasElements = RecommendedBookFrame.winfo_children()
    if FrameHasElements:
        for widget in RecommendedBookFrame.winfo_children():
            widget.destroy()

    query = f"""
            select "title id", titles, noofviews
            from bookinfo
            order by noofviews desc
            limit 10
        """

    cur.execute(query)
    TitleInfo = cur.fetchall()
    TitleInfolist = [e for e in TitleInfo]
    print(TitleInfolist)

    rank = 1
    if index <= 9:
        for Title in TitleInfolist:
            titles = TitleInfolist[index][1]
            BookID = TitleInfolist[index][0]
            noofviews = TitleInfolist[index][2]
            RankText = "#" + str(rank) + "\nViews: " + str(noofviews)

            ExistedTitleFrame[Title] = CTkFrame(RecommendedBookFrame, height=285, width=150, fg_color="transparent")
            ExistedTitleFrame[Title].grid(column=0, row=row, padx=10, pady=10, sticky="w")
            ExistedTitleLabel[Title] = CTkLabel(ExistedTitleFrame[Title], font=("Times", 14), text=titles,
                                                image=BookCover,
                                                wraplength=100)
            ExistedTitleLabel[Title].place(relx=-0.02, rely=-0.02)
            ExistedTitleLabel[Title].bind("<Button-1>",
                                          lambda e, bookid=BookID, TiTles=titles:
                                          ShowBookInfo(bookid, TiTles))
            NumberRank = CTkLabel(RecommendedBookFrame, text=RankText, font=("Consolas", 20),
                                  justify="left")
            NumberRank.grid(column=2, row=row)
            row += 1

            index += 1
            rank += 1


def RecommendedBooks():
    global query, titles
    ExistedTitleFrame = {}
    ExistedTitleLabel = {}
    index = 0
    row = 0
    column = 0

    RecommendedBookFrame = CTkScrollableFrame(MainWindow, height=300, width=750,
                                              label_text="RECOMMENDED FOR YOU",
                                              label_anchor="w",
                                              label_font=("Consolas", 30, "bold"),
                                              label_fg_color="transparent")
    RecommendedBookFrame.place(relx=0.165, rely=0.07)
    BookCover = CTkImage(light_image=Image.open("Book Front Cover.png"),
                         dark_image=Image.open("Book Front Cover.png"),
                         size=(165, 300))
    FrameHasElements = RecommendedBookFrame.winfo_children()
    if FrameHasElements:
        for widget in RecommendedBookFrame.winfo_children():
            widget.destroy()

    query = f"""
            select likedcategory from accountstatistics
            where id = '{GetLoginID}'
        """

    cur.execute(query)
    LikedCategory = cur.fetchall()
    Likedcategorylist = [e for e in LikedCategory]
    # stripping and separate items inside the text
    stripped = [value.strip(",") for value in Likedcategorylist[0]]
    clean = stripped[0].split(",")
    cleaned_list = [item.strip() for item in clean]

    for item in cleaned_list:
        query = f"""
                select "title id", titles from bookinfo
                where category like '%{item}%'
            """
        cur.execute(query)
        Titleinfo = cur.fetchall()
        TitleInfolist = [e for e in Titleinfo]

        for Title in TitleInfolist:
            titles = TitleInfolist[index][1]
            BookID = TitleInfolist[index][0]
            if column != 4:
                ExistedTitleFrame[Title] = CTkFrame(RecommendedBookFrame, height=285, width=150, fg_color="transparent")
                ExistedTitleFrame[Title].grid(column=column, row=row, padx=20, pady=10, sticky="w")
                ExistedTitleLabel[Title] = CTkLabel(ExistedTitleFrame[Title], font=("Times", 14), text=titles,
                                                    image=BookCover,
                                                    wraplength=100)
                ExistedTitleLabel[Title].place(relx=-0.02, rely=-0.02)
                ExistedTitleLabel[Title].bind("<Button-1>",
                                              lambda e, bookid=BookID, TiTles=titles:
                                              ShowBookInfo(bookid, TiTles))
                column += 1

            else:
                row += 1
                column = 0

                ExistedTitleFrame[Title] = CTkFrame(RecommendedBookFrame, height=285, width=150, fg_color="transparent")
                ExistedTitleFrame[Title].grid(column=column, row=row, padx=20, pady=10, sticky="w")
                ExistedTitleLabel[Title] = CTkLabel(ExistedTitleFrame[Title], font=("Times", 14), text=titles,
                                                    image=BookCover,
                                                    wraplength=100)
                ExistedTitleLabel[Title].place(relx=-0.02, rely=-0.02)

                column += 1

            # Make labels clikable
            # ExistedTitleLabel[Title].bind("<Button -1>", lambda e: ShowBookInfo(BookID, BookTitle))
            index += 1

        index = 0


AllBooks("All")
RetrievedPersonalData()
RecommendedBooks()
MostViedBooks()
ShoRecentViewed()

MainWindow.bind('<Return>', lambda e: AllBooks("Search"))
MainWindow.mainloop()
