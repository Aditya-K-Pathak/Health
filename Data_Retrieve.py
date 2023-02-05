import MySQLdb as msdb
import datetime

def month():
    currentDate = datetime.date.today()
    return currentDate.strftime("%B")[:3]

class Data:
    def __init__(self, user):
        self.name = user
        self.con = msdb.connect(host = "localhost", database = "User_Health_Data", user = "root", password = "070502")
        self.cursor = self.con.cursor()
        self.content = []

    def get_stats(self):
        data = self.cursor.execute(f"select * from {self.name}")
        data = self.cursor.fetchall()
        for i in data:
            self.content.append(i)
        # print(self.content)
        return self.content

    def get_steps(self):
        dates = []
        steps = []
        count = 0
        for i in range(-1,-7,-1):
            count += 1
            dates.append(self.content[i][0][0:6])
            # if count % 2 == 0:
            steps.append(self.content[i][1])
        print(dates)
        for i in range (5):
            for j in range (5):
                if int(dates[i][:2]) > int(dates[j][:2]):
                    dates[i], dates[j] = dates[j], dates[i]
                    steps[i], steps[j] = steps[j], steps[i]
        return (dates[::-1], steps[::-1])

    def get_cal(self):
        dates = []
        cal = []
        count = 0
        for i in range (-1, -7, -1):
            count += 1
            dates.append(self.content[i][0][0:6])
            # if count % 2 == 0:
            cal.append(self.content[i][2])
        for i in range (5):
            for j in range (5):
                if int(dates[i][:2]) > int(dates[j][:2]):
                    dates[i], dates[j] = dates[j], dates[i]
                    cal[i], cal[j] = cal[j], cal[i]
        return (dates[::-1], cal[::-1])

    def get_heart(self):
        dates = []
        cal = []
        count = 0
        for i in range(-1, -6, -1):
            count += 1
            dates.append(self.content[i][0][0:6])
            # if count % 2 == 0:
            cal.append(self.content[i][3])
        for i in range (5):
            for j in range (5):
                if int(dates[i][:2]) > int(dates[j][:2]):
                    dates[i], dates[j] = dates[j], dates[i]
                    cal[i], cal[j] = cal[j], cal[i]
        return (dates[::-1], cal[::-1])

class BioData:
    def __init__(self, user):
        self.name = user
        self.con = msdb.connect(host='localhost', user = 'root', database = "Auth_Data", password = "070502")
        self.cursor = self.con.cursor()

    def get_username(self):
        content = self.cursor.execute(f"select First_Name, Last_Name from Authentication_Data where UserName = '{self.name}'")
        row = self.cursor.fetchone()
        return (row[0], row[1])

# d = Data("aditya2874")
# d.get_stats()
# d.get_steps()