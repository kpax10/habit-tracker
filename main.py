import requests
from datetime import datetime

USERNAME = 'kpax10'
TOKEN = 'fh234hwe54'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

# graph_config = {
#     'id':'graph1',
#     'name': 'Exercise Graph',
#     'unit': 'commit',
#     'type': 'int',
#     'color': 'shibafu',
# }
#
# headers = {
#     'X-USER-TOKEN': TOKEN,
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# print(response.text)


# today = datetime.today().strftime('%Y%m%d')
# pixel_params = {
#     'date': '20241113',
#     'quantity': '1',
# }
#
# headers = {
#     'X-USER-TOKEN': TOKEN,
# }
#
# pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response)

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20241115"

headers = {
    'X-USER-TOKEN': TOKEN,
}

update_params = {
    'quantity': '0'
}

# response = requests.put(url=pixel_update_endpoint, json=update_params, headers=headers)
# print(response)

delete_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20241115"


response = requests.delete(url=delete_update_endpoint, headers=headers)
print(response.text)