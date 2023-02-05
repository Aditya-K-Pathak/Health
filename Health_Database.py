import requests
import MySQLdb as msdb

def update_data(username):
    try:
        url = "https://v1.nocodeapi.com/testapis/fit/IIFevNBIoYCoFLPx/aggregatesDatasets?dataTypeName=steps_count,active_minutes,calories_expended,heart_minutes,sleep_segment,weight,activity_summary"
        params = {}
        r = requests.get(url=url, params=params)
        json_data = r.json()
        # print(json_data)
    except:
        return -2

    lst = []
    con = msdb.connect(host="localhost", user="root",
                    database="User_Health_Data", password="070502")
    cursor = con.cursor()
    try:
        cmd = f"create table {username} (Time varchar(30), Steps int, Calories int, Heart int, Active_Minutes int)"
        cursor.execute(cmd)
    except:
        for i in json_data:
            for j in json_data[i]:
                st_time = j["startTime"]
                lst.append(st_time)
        lst.sort()
        lst = set(lst)
        a = []
        for i in lst:
            a = []
            for j in json_data:
                for k in json_data[j]:
                    # print(k)
                    if k["startTime"] == i:
                        if j == "steps_count" or j == "calories_expended" or j == "heart_minutes" or j == "active_minutes":
                            a += (j, k["value"])
            # print(a)
            
            try:
                steps = a[a.index("steps_count")+1]
            except ValueError:
                steps = 0
            try:
                cal = a[a.index("calories_expended")+1]
            except ValueError:
                cal = 0
            try:
                hp = a[a.index("heart_minutes")+1]
            except ValueError:
                hp = 0
            try:
                at = a[a.index("active_minutes")+1]
            except ValueError:
                at = 0
            cmd = f"insert into {username} values('{i[:11]}', {steps}, {cal}, {hp}, {at})"

            cursor = con.cursor()
            try:
                cursor.execute(cmd)
                con.commit()
            except msdb._exceptions.IntegrityError as e:
                print(e)
        return 1
# update_data("aditya2874")
# try:
#     url = "https://v1.nocodeapi.com/testapis/fit/IIFevNBIoYCoFLPx/aggregatesDatasets?dataTypeName=steps_count,active_minutes,calories_expended,heart_minutes,sleep_segment,weight,activity_summary"
#     params = {}   
#     r = requests.get(url=url, params=params)
#     json_data = r.json()
#     print(json_data)
# except:
#     print()