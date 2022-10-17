import asyncio
import aiohttp

async def multi_async():
    await asyncio.gather(*[get_name_async(f"img{i}.jpg") for i in range(1, 3 + 1)])


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
    async_start()
    async_start()
    async_start()
    # не уверен что правильно