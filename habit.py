# Pixela API

import requests
from datetime import datetime
import datetime

# print("\nTo see graph follow the link\n")
# print("https://pixe.la/v1/users/aditya2874/graphs/graph.html\n")
# print("1. Create a new user\n2. Create a graph\n3. Add data\n4. Update data\n5. Delete data")
# choice = int(input("Enter command to perform: "))
URL = "https://pixe.la/v1/users"
username = "aditya2874"
header = {
    "X-USER-TOKEN": "8840207363"
}
graph_name = "Python"
graph_id = "graph"

User_Parameter = {
    "token": header,
    "username": username,
    "agreeTermsOfService": "yes",
    "notminor": "yes",
}

Graph_Parameters = {
    "id": "graph",
    "name": "Python",
    "unit": "minute",
    "type": "float",
    "color": "ajisai",
}
# Graph_Parameters = {
#     "id": "graph",
#     "name": "Python",
#     "unit": "minute",
#     "type": "float",
#     "color": "ajisai",
#     "date": "20210805",
# }

# print()
# REtuurns list of pixels' dates

# for i in data["pixels"]:
    # dates.append(i)

# Retuns resukts as {"totalPixelsCount":368,"maxQuantity":120,"minQuantity":55,"totalQuantity":32501,"avgQuantity":88.32,"todaysQuantity":0}
def Overall_data():
    url = f"{URL}/{username}/graphs/{graph_id}/stats"
    # print(url)
    response = requests.get(url)
    response = response.json()
    return response
# 
def Weekly_Stats():
    response = requests.get(url = f"{URL}/{username}/graphs/{graph_id}/pixels", headers=header)
    # print(response.text)
    data = response.json()
    dates = []
    for i in range (-1,-8,-1):
        dates.append(data["pixels"][i])
    time = []
    for date in dates:
        response = requests.get(url = f"{URL}/{username}/graphs/{graph_id}/{date}", headers = header)
        response = response.json()
        time.append(float(response["quantity"]))
    dates = []
    for i in range (-1,-8,-1):
        d = datetime.datetime.strptime(data["pixels"][i], "%Y%m%d")
        s = d.strftime('%d %b')
        dates.append(s)
    return dates[::-1], time[::-1]


# if choice == 1:
#     try:
#         response = requests.post(url=URL, json=User_Parameter)
#         print(response.text)
#     except:
#         print("Some Error Occured...!\nTry checking your Connection...")
#     else:
#         print("User was created successfully...")

# elif choice == 2:
#     try:
#         # print( f"{url}/{username}/graphs")
#         response = requests.post(
#             url=f"{URL}/{username}/graphs", json=Graph_Parameters, headers=header)
#         print(response.text)
#     except:
#         print(f"Some Error Occured...!\nTry checking your Connection...")
#     else:
#         print("Successfully created your graph...")

# elif choice == 3:
#     try:
#         today = datetime.now()
#         quantity = int(input("Enter how many minutes: "))
#         parameter = {
#             "date": today.strftime("%Y%m%d"),
#             "quantity": f"{quantity}",
#         }
#         response = requests.post(
#             url=f"{URL}/{username}/graphs/{graph_id}", json=parameter, headers=header)
#     except:
#         print("Some Error Occured...!\nTry checking your Connection...")
#     else:
#         print("Successfully added today's data of yours'...")

# elif choice == 4:
#     try:
#         year = input("Enter year: ")
#         month = input("Enter Month: ")
#         date = input("Enter date: ")
#         minutes = input("Enter how many minutes: ")
#         day = year+month+date
#         parameter = {
#             "quantity": f"{minutes}"
#         }
#         response = requests.put(
#             url=f"{URL}/{username}/graphs/{graph_id}/{day}", json=parameter, headers=header)
#         print(response.text)
#     except:
#         print("Some Error Occured...!\nTry checking your Connection...")
#         print(response.text)
#     else:
#         print("Successfully updated your data...")

# elif choice == 5:
#     try:
#         response = requests.delete(
#             url=f"{URL}/{username}/graphs/{graph_id}", headers=header)
#         print(response.text)
#     except:
#         print("Some Error Occured...")
#     else:
#         print("Invalid input...")
