# Will be used to get username and password to delete data

import MySQLdb as msdb


class DeleteUser:
    def __init__(self, username, password):
        self.name = username
        self.password = password
        self.con_to_auth = msdb.connect(
            host="localhost", user="root", database="auth_data", password="070502")
        self.con_to_health = msdb.connect(
            host="localhost", user="root", database="User_Health_Data", password="070502")
        self.con_to_loc = msdb.connect(
            host="localhost", user="root", database="location_data", password="070502")

    def delete_from_auth(self):
        cursor = self.con_to_auth.cursor()
        cmd = f"DELETE FROM authentication_data where UserName = '{self.name}' and Password = '{self.password}'"
        cursor.execute(cmd)
        self.con_to_auth.commit()

    def delete_from_health(self):
        cursor = self.con_to_health.cursor()
        cmd = f"DROP TABLE {self.name}"
        cursor.execute(cmd)
        self.con_to_health.commit()

    def delete_from_loc(self):
        cursor = self.con_to_loc.cursor()
        cmd = f"DROP TABLE {self.name}"
        cursor.execute(cmd)
        self.con_to_loc.commit()
