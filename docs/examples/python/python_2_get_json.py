
import requests

url = 'https://iothook.com/api/v1.2/datas/'
auth=('anonymoususer', 'a12345678')

response = requests.get(url, auth=auth)
data = response.json()
print data
