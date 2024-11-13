import requests

USERNAME = 'kpax10'
TOKEN = 'fh234hwe54'

pixela_endpoint = 'https://pixe.la/v1/users'

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
