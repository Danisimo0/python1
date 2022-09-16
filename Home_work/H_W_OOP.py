import requests
import json
import os

# много пыхтел, многое опробовал, но все равно не понял в чем ошибка и тд, сначала была ошибка, а теперь None


def download_img(url='https://jsonplaceholder.typicode.com/photos'):
    try:
        response = requests.get(url=url)
        with open('file_name', 'wb') as file:
            file.write(response.content)

    except Exception as _ex:
        return 'error'


def main():
    print(download_img(url='https://jsonplaceholder.typicode.com/photos'))


if __name__ == '__main__':
    main()


# # url = "https://jsonplaceholder.typicode.com/photos/1"
# #
# # photo = requests.get(url=url)
# # print((photo.json()))
# #
# # photos_list = photo.json()
# # for photo in photos_list:
# #     with open(f"python_photo/photo{photo['id']}.json", mode="w") as file:
# #         json.dump((photo), fp=file)
# #
# # with open("photo.json", mode="rb") as file:
# #     json1 = json.load(file)
# #     print(json1)
#
#
#
#
#
#

# import json
# import requests
#

# # HTTP  - GET POST PUT(PUTCH) DELETE (CRUD)
#
# response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")
# print(response)
#
#
# # response = requests.get(url="https://jsonplaceholder.typicode.com/todos/1")
# # print(response.content)
# # print(type(response.content))
# # dictionary2 = json.loads(response.content)  # позволяет сериализовать строку или байтовую строку в словарь
# # print(dictionary2)
# # print(type(dictionary2))
#
# with open('new1.json', mode='w') as file:
#     dict3 = {
#         "userId": 1,
#         "id": 1,
#         "title": "delectus aut autem",
#         "completed": [
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             },
#             {
#                 "userId": 1,
#                 "id": 1,
#                 "title": "delectus aut autem",
#                 "completed": False
#             }
#         ]
#     }
# json.dump(dict3, file)  # позволяет записать объект JSON в файл
# ret = json.dumps(dict3)  # сериализует объект JSON в строку, которую можно без потерь записать в файл
# print(ret)
# print(type(ret))
# file.write(ret)



# def download_img(url='https://jsonplaceholder.typicode.com/photos'):
#     file_name = url.split("/")[-1]
#     print(file_name)
#     response = requests.get(url)
#     open(file_name, "wb").write(response.content)
#
#
# download_img()


