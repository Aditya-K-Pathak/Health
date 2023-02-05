import MySQLdb as msdb

class Location:
    def __init__(self, user):
        self.name = user
        self.con = msdb.connect(host = "localhost", user = "root", database = "Location_Data", password = "070502")
        self.cursor = self.con.cursor()
        self.content = []
    
    def create_user(self):
        cmd = f"create table {self.name} (Time varchar(30) UNIQUE, Latitude float, Longitude float, PIN int, City char(30), Ip_Address varchar(50), Carrier char(20))"
        try:
            self.cursor.execute(cmd)
            self.con.commit()
            return 1
        except Exception as e:
            return e

    def insert(self, time, lat, lon, pin, city, ip, car):
        cmd = f"insert into {self.name} values('{time}', {lat}, {lon}, {pin}, '{city}', '{ip}', '{car}')"
        self.cursor.execute(cmd)
        self.con.commit()

    def get_location(self, user):
        cmd = f"select * from {user}"
        self.cursor.execute(cmd)
        data = self.cursor.fetchall()
        for i in data:
            self.content.append(i)
        return self.content
