# class Auto:
#     def __init__(self, model, year, engine, color, price):
#         self.model = model
#         self.year = year
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def print_(self):
#         print(
#             f'Модель {self.model} {self.year} года выпуска с объемом двигателя {self.engine} литра цвета {self.color} и стоимости {self.price} dollars')
#
#     def change_model(self, new_model):
#         self.model = new_model
#
#     def change_year(self, new_year):
#         self.year = new_year
#
#     def change_engine(self, new_engine):
#         self.engine = new_engine
#
#     def change_color(self, new_color):
#         self.color = new_color
#
#     def change_price(self, new_price):
#         self.price = new_price


# 2
# class Book:
#     def __init__(self, name, year, publisher, genre, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.price = price
#
#     def print_(self):
#         print(
#             f'Название {self.name} {self.year} года выпуска {self.publisher} издатель жанр {self.genre} и  {self.price}  dollars')
#
#
#     def change_book(self, new_book):
#         self.name = new_name
#
#     def change_year(self, new_year):
#         self.year = new_year
#
#     def change_publisher(self, new_publisher):
#         self.publisher= new_publisher
#
#     def change_genre(self, new_genre):
#         self.genre = new_genre
#
#     def change_price(self, new_price):
#         self.price = new_price


# 3


class Stadion:
    def __init__(self, name, year, country, city, capacity):
        self.name = name
        self.year = year
        self.country = country
        self.city = city
        self.capacity = capacity

    def print_(self):
        print(
            f'Название {self.name} {self.year} дата открытия {self.country} страна город {self.city} и  {self.capacity}  вместимость')

    def change_stadion(self, new_stadion):
        self.name = new_name

    def change_year(self, new_year):
        self.year = new_year

    def change_country(self, new_country):
        self.country = new_country

    def change_city(self, new_city):
        self.city = new_city

    def change_capacity(self, new_capacity):
        self.capacity = new_capacity

# остальные вроде повторяются 
