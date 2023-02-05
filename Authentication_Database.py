import MySQLdb as Msdb


class DataBase:
    def __init__(self, username, password):
        self.name = username
        self.pin = password
        self.con = Msdb.connect(
            host="localhost", database="auth_data", user="root", password="070502")
        self.cursor = self.con.cursor()

    def Create_User(self, first_name, last_name, email, phone, em_phone, em_mail):
        cmd = f"insert into Authentication_Data values('{self.name}','{self.pin}', '{first_name}', '{last_name}', {phone}, '{email}', {em_phone}, '{em_mail}')"
        try:
            self.cursor.execute(cmd)
            self.con.commit()
            return 1
        except Exception as e:
            e = str(e)
            if "Duplicate" in e:
                return 2
            elif "Unknown" in e:
                return 3
            return 0

    def Delete_User(self):
        cmd = f"delete from Authentication_Data where username = '{self.name}'"
        try:
            self.cursor.execute(cmd)
            self.con.commit()
        except Exception as e:
            print(e)

    def log_in(self):
        cmd = f"select * from Authentication_Data where username = '{self.name}'"
        self.cursor.execute(cmd)
        content = self.cursor.fetchone()
        if self.cursor.rowcount != 0:
            if content[1] == self.pin:
                return 1
            else:
                return 2
        else:
            return 0
