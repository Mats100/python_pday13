import requests
from datetime import datetime

USERNAME = "mats"
TOKEN = "ghdffaukakwuawui"
GRAPH_ID ="graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notminor":"yes",
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id":GRAPH_ID,
    "name":"Cyling Graph",
    "unit":"miles",
    "type":"int",
    "color":"kuro"
}

headers = {
    "X-USER-TOKEN":TOKEN
}
# response =requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022,month=8,day=13)
# print(today.strftime("%Y-%m-%d"))

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"15",
}
response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)









