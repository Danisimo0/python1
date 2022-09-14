import asyncio
import requests
from bs4 import BeautifulSoup
import aiohttp
import os

# 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/102.0.0.0 Safari/537.36'
}
url = 'https://kurs.kz'
response = requests.get(urlm, headers=headers)
# print(response)

bs = BeautifulSoup(response.text, "lxml")
# print(bs)


print(Search)

# 2

# photo = requests.get(url="https://jsonplaceholder.typicode.com/photos")
#
# photos_list = photo.json()
#
# for key, val in photos_list.items():
#     print(f"{key}: {val}")
#


r = requests.get('https://jsonplaceholder.typicode.com/photos')
html = r.text


def find(html):
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find('div', class_='cards')
    row = div.find_all('img')

    links = [col['src'][2:] for col in row]

    return links
