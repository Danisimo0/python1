import requests
import json
import os


# много пыхтел, многое опробовал, но все равно не понял в чем ошибка и тд,получаю только json объект



def download_img(url='https://jsonplaceholder.typicode.com/photos/1'):
    try:
        response = requests.get(url=url)
        with open('new.json', 'wb') as file:
            file.write(response.content)

        with open('new.json', mode='w') as file:
            dict3 = {
                "userId": 1,
                "id": 1,
                "title": "delectus aut autem",
                "completed": [
                    {
                        "userId": 1,
                        "id": 1,
                        "title": "delectus aut autem",
                        "completed": False
                    },
                    {
                        "userId": 1,
                        "id": 1,
                        "title": "delectus aut autem",
                        "completed": False
                    },
                    {
                        "userId": 1,
                        "id": 1,
                        "title": "delectus aut autem",
                        "completed": False
                    }
                ]
            }
            # есть предположение что здесь не правильно записываю

            ret = json.dumps(dict3)
            print(ret)
            file.write(ret)


    except Exception as _ex:
        return 'error'


download_img()



# ниже все мои попытки не верные


# def download_img(url='https://jsonplaceholder.typicode.com/photos'):
#     photo = requests.get(url)
#     photos_list = photo.json()
#     for photo in photo_list:
#         with open(f'Home_work/photo{photo["id"]}.json', mode="w") as file:
#             json.dump(photo)
#     with open("photo.json", mode="rb") as file:
#         json1 = json.load(file)
#         print(json1)
#
#
# download_img()

# photo = requests.get(url="https://jsonplaceholder.typicode.com/photos%22")
# print((photo.json()))
#
# photos_list = photo.json()
# for photo in photos_list:
#     with open(f"python_photo/photo{photo['id']}.json", mode="w") as file:
#         json.dump((photo), fp=file)
#
# with open("photo.json", mode="rb") as file:
#     json1 = json.load(file)
#     print(json1)


# def download_img(url='https://jsonplaceholder.typicode.com/photos'):
#     try:
#         response = requests.get(url=url)
#         with open('new2.img', 'wb') as file:
#             file.write(response.content)
#
#     except Exception as _ex:
#         return 'error'
#
#
# download_img()

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
