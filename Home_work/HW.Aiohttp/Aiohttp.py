import requests
from bs4 import BeautifulSoup

# 1

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }
#
# url = 'https://myfin.by/converter'
#
# responce = requests.get(url)
# bs = BeautifulSoup(responce.text, 'html.parser')
#
# table = bs.find_all('div', {'class': 'record vis_nbrbusd'})
# print(table)


# 2

#
# async def as_write_image_from_url(image_name: str) -> None:
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://picsum.photos/600/600/') as clien_response:
#             response = await clien_response.read()
#
#     with open(f'images/{image_name}.jpg', mode='wb') as file:
#         file.write(response)
#
#
# async def async_download():
#     await asyncio.gather(*[as_write_image_from_url(f'img{i}') for i in range(1 + 1)])
#
#
# def async_download_image():
#     asyncio.run(async_download())
# еще затрудняюсь с этим, взял с классной работы


# 3


responce = requests.get('https://www.zakon.kz/pogoda/almaty/')
# print(responce)
bs = BeautifulSoup(responce.text, 'html.parser')
html = bs.find_all('div', {'class': 'seven-days_temp'})
objs4 = [x.text.strip() for x in html]

print(f"{'today'}: The september of 23 ; day: {objs4[1]} | night: {objs4[1]}\n")
# ну мог немного по другому сделать и уже нормально данные вывести, но думаю так тоже сойдет
