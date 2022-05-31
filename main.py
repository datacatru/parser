import requests

url = 'https://medicinadeti.ru/'
req = requests.get(url)

if '50703166' in req.text:
    print('YM is find')
