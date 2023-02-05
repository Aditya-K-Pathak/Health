from tkinter import *
from matplotlib.figure import Figure
import Data_Retrieve as dr  
import habit
import Location_Database as ldb
import webbrowser
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)


Username = "aditya2874"
ovr_all_data = habit.Overall_data()
weekly_stats = habit.Weekly_Stats()

ldb = ldb.Location(Username)
loc = ldb.get_location(Username)

def callback(url):
        webbrowser.open_new_tab(url)

def User(username):
    root = Tk()
    root.title(f"{username}")
    root.minsize(1366, 768)
    root.config(bg="black")
    # root.attributes(fullscreen = True)

    title = dr.BioData(f"{username}")
    title = title.get_username()
    Name = f"{title[0]}"
    Label(text=f"Hi! {Name}", font=("Algerian", 40, "underline"),
          foreground="red", background="black").place(x=10, y=20)

    can = Canvas(root, width=1366/4, height=200,
                 border="0", background="black")
    can.place(x=1000, y=0)
    Label(text="Steps", font=("Bell MT", 18), foreground="white",
          background="black").place(x=900, y=102)

    fig = Figure(figsize=(6, 4),
                 dpi=60)

    plot1 = fig.add_subplot()

    user = dr.Data(f"{username}")
    user.get_stats()
    content = user.get_steps()
    plot1.plot(content[0], content[1],)
    # plot1.title("Steps Count")

    canvas = FigureCanvasTkAgg(fig,
                               master=can)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=-10, y=-26)

    can = Canvas(root, width=1366/4, height=220,
                 border="0", background="black")
    can.place(x=1000, y=240)
    Label(text="Calories", font=("Bell MT", 18), foreground="white",
          background="black").place(x=900, y=350)

    fig = Figure(figsize=(6, 4),
                 dpi=60)

    plot1 = fig.add_subplot()

    user = dr.Data(f"{username}")
    user.get_stats()
    content = user.get_cal()
    plot1.plot(content[0], content[1],)

    canvas = FigureCanvasTkAgg(fig,
                               master=can)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=-10, y=-10)

    can = Canvas(root, width=1366/4, height=220,
                 border="0", background="black")
    can.place(x=1000, y=500)
    Label(text="Heart Point", font=("Bell MT", 18),
          foreground="white", background="black").place(x=877, y=620)

    fig = Figure(figsize=(6, 4),
                 dpi=60)

    plot1 = fig.add_subplot()

    user = dr.Data(f"{username}")
    user.get_stats()
    content = user.get_heart()
    plot1.plot(content[0], content[1],)

    canvas = FigureCanvasTkAgg(fig,
                               master=can)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=-10, y=-10)

# Graph for weekly habit

    can = Canvas(root, width=1366/4, height=220,
                 border="0", background="black")
    can.place(x=20, y=470)
    Label(text="Weekly Habit Track", font=("Bell MT", 18),
          foreground="white", background="black").place(x=85, y=700)
    fig = Figure(figsize=(6, 4),
                 dpi=60)

    plot1 = fig.add_subplot()
    plot1.plot(weekly_stats[0], weekly_stats[1],)

    canvas = FigureCanvasTkAgg(fig,
                               master=can)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().place(x=-10, y=-10)

    Label(text="Overall Habit Data", font=("Bell MT", 18, "underline"), foreground="white",
          background="black").place(x=10, y=120)

    Label(text=f"Hi {Name}, here is your weekly data of Steps, Calories, Heart points, and Habit.", font=(
        "Centaur", 14), foreground="white", background="black", justify="left",).place(x=10, y=80)
    Label(text=f"Your total Pixel count is {ovr_all_data['totalPixelsCount']}, \n>>> Maximum time spent is {ovr_all_data['maxQuantity']} minutes while \n>>> Minimum time spent is {ovr_all_data['minQuantity']} minutes, \nAnd your Average is {ovr_all_data['avgQuantity']} minutes.", font=(
        "Centaur", 14), foreground="white", background="black", justify="left",).place(x=10, y=150)

    Label(text="Weekly Habit Data", font=("Bell MT", 18, "underline"), foreground="white",
          background="black").place(x=10, y=250)

    Label(text=f">>> Maximum time spent is {int(max(weekly_stats[1]))}minutes while \n>>> Minimum time spent is {int(min(weekly_stats[1]))} minutes, \nAnd your Average is {int(sum(weekly_stats[1])/7)} minutes.", font=(
        "Centaur", 14), foreground="white", background="black", justify="left",).place(x=10, y=280)

    Label(text=f"Your Last two known locations are as follow:\n1) Latitude: {loc[-1][1]} Longitude: {loc[-1][2]} at Location {loc[-1][4]}, by IP address: {loc[-1][-2]} & provider {loc[-1][-1]}.\n2) Latitude: {loc[-2][1]} Longitude: {loc[-2][2]} at Location {loc[-2][4]}, by IP address: {loc[-2][-2]} & provider {loc[-2][-1]}.", font=(
        "Centaur", 14), foreground="white", background="black", justify="left",).place(x=10, y=350)

    Label(text=f"See your graph by clicking ", font=(
        "Centaur", 14), foreground="white", background="black", justify="left",).place(x=10, y=420)


    # Create a Label to display the link
    link = Label(text="here", font=(
        "Centaur", 14, "underline"), foreground="blue", background="black", justify="left",)
    link.place(x = 200, y = 420)
    link.bind("<Button-1>", lambda e:
    callback("https://pixe.la/v1/users/aditya2874/graphs/graph.html"))



    root.mainloop()


User(Username)
