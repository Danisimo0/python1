import asyncio
import requests
from bs4 import BeautifulSoup


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                   'AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/102.0.0.0 Safari/537.36'
# }



# response = requests.get(url=" ", headers=headers)
# print(response.text)



def multi():
    current_thread = 16
    with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread * 2 + 1) as executor:
        for x in range(1, 10 + 1):
            executor.submit(get_name, f'img{x}.jpg')


async def multi_async():
    await asyncio.gather(*[get_name_async(f"img{i}.jpg") for i in range(1, 10 + 1)])


async def get_name_async(file_name: str) -> None:
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://picsum.photos/600/600/", headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }

                               ) as request:
            response = await request.read()

    with open(file_name, "wb") as file:
        file.write(response)


def async_start():
    asyncio.run(multi_async())


if __name__ == '__main__':
    # get_name()
    # multi()
    async_start()



