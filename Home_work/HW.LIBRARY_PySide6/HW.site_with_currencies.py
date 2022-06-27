import PySide6
import requests

url = "https://myfin.by/converter"
headers = {'User-agent': 'your bot 0.1'}    # "my-app/0.0.1"
response = requests.get(url=url, headers=headers)


url = response.content
with open(file='new.html', mode="wb") as file:
    file.write(url)


