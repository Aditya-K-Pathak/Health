import json
import requests
import Location_Database as ldb

def loc(username):
    api_key = "xn31p6uc7coycvh7"

    response = requests.get(f"https://api.ipregistry.co/?key={api_key}")
    content = response.content
    content = json.loads(content.decode())
    d = {
        username: 
        {
            content["time_zone"]["current_time"]:
            {
                "lat": content["location"]["latitude"],
                "lon": content["location"]["longitude"],
                "post": content["location"]["postal"],
                "city": content["location"]["city"],
                "carrier": content["carrier"]["name"],
                "IP": content["ip"]
            }
        }
    }
    return d

def insert_data(username):
    d = loc(username)
    user = ldb.Location(username)
    time = ""
    for i in d[username]:
        time = i
    eas = d[username][time]
    user.insert(time, eas["lat"], eas["lon"], eas["post"], eas["city"], eas["IP"], eas["carrier"])
    # print(time)

# insert_data("aditya2874")