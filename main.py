from tkinter import *
from tkinter import messagebox as tmsg
from PIL import Image, ImageTk
import Authentication_Database as adb
import Location_Database as ldb
import Health_Database as hdb
import Del_Data as ddata
import Dashboard as dsbd
import Location

HEADING_FONT = ("Algerian", 36)
LABEL_FONT = ("Gabriola", 20, "bold")
ENTRY_FONT = ("Bell MT", 13)
USERNAME = ""
PASSWORD = ""
FIRST_NAME = ""
LAST_NAME = ""
EMAIL = ""
PHONE = int()
EMERGENCY_PHONE = int()
EMERGENCY_MAIL = ""


def login():
    def Check_Validity():
        user_name = USERNAME.get()
        user_pass = PASSWORD.get()
        if " " in user_name or user_name == "":
            tmsg.showerror(
                "Format Error", "Kindly Correct your format for Username, it shouln't contain Spaces or left blank")
            une.delete(0, END)
            upe.delete(0, END)
        elif " " in user_pass or user_pass == "":
            tmsg.showerror(
                "Format Error", "Kindly Correct your format for Password, it shouln't contain Spaces or left blank")
            une.delete(0, END)
            upe.delete(0, END)
        else:
            user = adb.DataBase(user_name, user_pass)
            response = user.log_in()
            if response == 0:
                tmsg.showerror(
                    "User Error", "No Such User exist, Kindly Sign up.")
                une.delete(0, END)
                upe.delete(0, END)
            elif response == 2:
                tmsg.showerror("Invalid Credentials",
                               "Invalid Password, kindly recheck your password.")
                upe.delete(0, END)
            else:
                Location.insert_data(user_name)
                hdb.update_data(user_name)
                # tmsg.showinfo("Welcome", "Welcome")
                root.destroy()
                try:
                    dsbd.User(user_name)
                except ConnectionError as e:
                    tmsg.showerror(f"{e}", "No internet access.")

    can = Canvas(root, width=1366/4, height=768 /
                 2, border="0", background="black")
    can.place(x=(1366-(1366/4))/4, y=(768-(768/2))/1.8)
    label = Label(can, text="Enter your Details", foreground="Red",
                  anchor="n", width="23", font=("Times New Roman", 20))
    label.place(x=2, y=0)

    Label(can, text="Username", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=50)
    Label(can, text="Password", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=120)
    Label(can, text="_"*59, foreground="white",
          background="black").place(x=30, y=105)
    Label(can, text="_"*59, foreground="white",
          background="black").place(x=30, y=175)

    USERNAME = StringVar()
    PASSWORD = StringVar()
    une = Entry(can, textvariable=USERNAME, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    upe = Entry(can, textvariable=PASSWORD, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    une.place(x=30, y=90, height=30, width=300)
    upe.place(x=30, y=160, height=30, width=300)
    Button(can, text="Submit", command=Check_Validity, borderwidth=0, foreground="white",
           background="black", activeforeground="gray").place(x=150, y=250)
    can.bind("<Return>", Check_Validity)


def Sign_Up():

    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRST_NAME = StringVar()
    LAST_NAME = StringVar()
    PHONE = StringVar()
    EMAIL = StringVar()
    EMERGENCY_PHONE = StringVar()
    EMERGENCY_MAIL = StringVar()

    def Submit():
        username = USERNAME.get()
        pin = PASSWORD.get()
        fname = FIRST_NAME.get()
        lname = LAST_NAME.get()
        mail = EMAIL.get()
        phone = PHONE.get()
        em_mail = EMERGENCY_MAIL.get()
        em_phone = EMERGENCY_PHONE.get()
        if em_mail == "" or em_phone == "":
            tmsg.showerror("Empty", "Emergency Informations Cannot be Empty.")
            Second_Step()
        elif " " in em_mail or " " in em_phone:
            tmsg.showerror(
                "Space", "No Spaces are allowed in Emergency Informations.")
            Second_Step()
        else:
            user = adb.DataBase(username, pin)
            user_location = ldb.Location(username)
            health_response = hdb.update_data(username)
            response = user.Create_User(
                fname, lname, mail, phone, em_phone, em_mail)
            location_response = user_location.create_user()
            Location.insert_data(username)
            if response == 1 and location_response == 1 and health_response == 1:
                tmsg.showinfo("User Created",
                              "User Created Successfully\nKindly Login")
            elif response == 2:
                tmsg.showwarning(
                    "Username Error", "Username already Exist.\n Try Unique Username")
            elif response == 3:
                tmsg.showwarning(
                    "Format Error", "Please Check Format of Your Entry.")
            elif health_response == -2:
                tmsg.showerror("Network Connection Error",
                               "No internet access, Kindly check your connection and try again...")
            else:
                tmsg.showerror("Error", "Some Error Occured")

    def Second_Step():
        username = USERNAME.get()
        pin = PASSWORD.get()
        fname = FIRST_NAME.get()
        lname = LAST_NAME.get()
        if username == "" or pin == "" or fname == "" or lname == "":
            Sign_Up()
            tmsg.showerror("Empty Field", "All fields are mandatory.")
        elif " " in username:
            Sign_Up()
            tmsg.showerror("UserName Error", "Username Cannot contain Spaces.")
        elif " " in pin:
            Sign_Up()
            tmsg.showerror("Password Error", "Password Cannot contain Spaces.")
        else:
            can = Canvas(root, width=1366/4, height=768 /
                         2, border="0", background="black")
            can.place(x=(1366-(1366/4))/4, y=(768-(768/2))/1.8)
            label = Label(can, text="Enter Details for Emergency!", foreground="Red",
                          width="24", font=("Times New Roman", 20))
            label.place(x=2, y=0)

            Label(can, text="Emergency Contact Number", font=(LABEL_FONT),
                  foreground="white", background="black").place(x=25, y=50)
            Label(can, text="Emergency E-Mail Id.", font=(LABEL_FONT),
                  foreground="white", background="black").place(x=25, y=120)
            Label(can, text="_"*50, foreground="white",
                  background="black").place(x=28, y=105)
            Label(can, text="_"*50, foreground="white",
                  background="black").place(x=30, y=175)

            em_ph = Entry(can, textvariable=EMERGENCY_PHONE, borderwidth=0,
                          font=ENTRY_FONT, foreground="white", background="black",)
            em_mail = Entry(can, textvariable=EMERGENCY_MAIL, borderwidth=0,
                            font=ENTRY_FONT, foreground="white", background="black",)
            em_ph.place(x=30, y=90, height=30, width=255)
            em_mail.place(x=30, y=160, height=30, width=255)
            btn = Button(can, text="Submit", command=Submit, borderwidth=0, foreground="white",
                         background="blue", activeforeground="gray")
            btn.place(x=150, y=250)

    can = Canvas(root, width=1366/4, height=768 /
                 2, border="0", background="black")
    can.place(x=(1366-(1366/4))/4, y=(768-(768/2))/1.8)
    label = Label(can, text="Welcome New User!", foreground="Red",
                  anchor="n", width="23", font=("Times New Roman", 20))
    label.place(x=2, y=0)

    Label(can, text="Username", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=50)
    Label(can, text="Password", font=(LABEL_FONT),
          foreground="white", background="black").place(x=190, y=50)
    Label(can, text="First Name", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=120)
    Label(can, text="Last Name", font=(LABEL_FONT),
          foreground="white", background="black").place(x=190, y=120)
    Label(can, text="Contact No.", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=190)
    Label(can, text="E-Mail Id.", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=260)
    Label(can, text="_"*26+" "*9+"_"*26, foreground="white",
          background="black").place(x=28, y=105)
    Label(can, text="_"*26+" "*9+"_"*26, foreground="white",
          background="black").place(x=30, y=175)
    Label(can, text="_"*50, foreground="white",
          background="black").place(x=30, y=245)
    Label(can, text="_"*50, foreground="white",
          background="black").place(x=30, y=315)

    une = Entry(can, textvariable=USERNAME, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    upe = Entry(can, textvariable=PASSWORD, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    une.place(x=30, y=90, height=30, width=130)
    upe.place(x=190, y=90, height=30, width=130)

    fn = Entry(can, textvariable=FIRST_NAME, borderwidth=0,
               font=ENTRY_FONT, foreground="white", background="black",)
    ln = Entry(can, textvariable=LAST_NAME, borderwidth=0,
               font=ENTRY_FONT, foreground="white", background="black",)
    fn.place(x=30, y=160, height=30, width=130)
    ln.place(x=190, y=160, height=30, width=130)

    ph = Entry(can, textvariable=PHONE, borderwidth=0,
               font=ENTRY_FONT, foreground="white", background="black",)
    mail = Entry(can, textvariable=EMAIL, borderwidth=0,
                 font=ENTRY_FONT, foreground="white", background="black",)
    ph.place(x=30, y=230, height=30, width=255)
    mail.place(x=30, y=300, height=30, width=255)

    Button(can, text="Second Step", command=Second_Step, borderwidth=0, foreground="white",
           background="black", activeforeground="gray").place(x=150, y=350)


def delete_data():
    def del_data():
        username = USERNAME.get()
        password = PASSWORD.get()
        user = adb.DataBase(username, password)
        response = user.log_in()
        if response == 1:
            user = ddata.DeleteUser(username, password)
            user.delete_from_auth()
            user.delete_from_health()
            user.delete_from_loc()
            tmsg.showinfo("User Deleted",
                          f"User {username} deleted Successfully...")
        elif response == 2:
            tmsg.showerror("Wrong password", "Please Enter a valid Password")
        elif response == 0:
            tmsg.showerror("User Not Found", "No Such User found...")
    can = Canvas(root, width=1366/4, height=768 /
                 2, border="0", background="black")
    can.place(x=(1366-(1366/4))/4, y=(768-(768/2))/1.8)
    label = Label(can, text="Enter UserName & Password", foreground="Red",
                  anchor="n", width="23", font=("Times New Roman", 20))
    label.place(x=2, y=0)

    Label(can, text="Username", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=50)
    Label(can, text="Password", font=(LABEL_FONT),
          foreground="white", background="black").place(x=25, y=120)
    Label(can, text="_"*59, foreground="white",
          background="black").place(x=30, y=105)
    Label(can, text="_"*59, foreground="white",
          background="black").place(x=30, y=175)

    USERNAME = StringVar()
    PASSWORD = StringVar()
    une = Entry(can, textvariable=USERNAME, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    upe = Entry(can, textvariable=PASSWORD, borderwidth=0,
                font=ENTRY_FONT, foreground="white", background="black",)
    une.place(x=30, y=90, height=30, width=300)
    upe.place(x=30, y=160, height=30, width=300)
    Button(can, text="Submit", borderwidth=0, command=del_data, foreground="white",
           background="black", activeforeground="gray").place(x=150, y=250)


root = Tk()
root.maxsize(1366, 768)
root.geometry("1366x768")
root.title("Fitness-Habit Tracker")

image = Image.open("Resources/background.jpg")
pic = ImageTk.PhotoImage(image)
label = Label(image=pic)
label.pack()

Login = Label(text="Welcome User...", foreground="red",
              background="black", font=HEADING_FONT)
Login.place(x=230, y=105)

login_btn = Button(text="Login", command=login, foreground="white", background="black", font=(
    "consolas", 20), borderwidth=0, width=int((136/4)/3), activebackground="white", activeforeground="black",)
login_btn.place(x=265, y=155)

del_user = Button(text="Delete User", command=delete_data, foreground="white", background="black", font=(
    "consolas", 20), borderwidth=0, width=int((136/4)/3), activebackground="white", activeforeground="black",)
del_user.place(x=10, y=700)

signup_btn = Button(text="Sign Up", command=Sign_Up, foreground="white", background="black", font=(
    "consolas", 20), borderwidth=0, width=int((136/4)/3), activebackground="gray", activeforeground="black")
signup_btn.place(x=415, y=155)

root.mainloop()
