import requests

n = requests.get('https://api.github.com')
#response.status_code

if n.status_code == 200:
    print('Success!')
elif n.status_code == 404:
    print('Not Found.')