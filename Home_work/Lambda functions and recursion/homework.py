# Задача 1
# days = int(input('Введите день: '))
# weeks = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
# print(weeks[days-1])


# Задача 2
#
# number = int(input("Введите номер месяца: "))
# months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
#
# if number >= 13:
#     print("Вы можете набрать число от 1 до 12!")
# else:
#     print(months[number - 1])


# Задача 3

# number = int(input("Введите число: "))
# if number > 0:
#     print("Number is positive")
# elif number < 0:
#     print("Number is negative")
# else:
#     print("Number is equal to zero")
#

# Задача 4
#
# number1 = int(input("Введите 1 чиcло: "))
# number2 = int(input("Введите 2 чиcло: "))
# if number1 == number2:
#     print(number1, number2)
#
# else:
#     print(min(number1, number2))
#     print(max(number1, number2))


# Задача 5

# a = int(input("Введите 1 число: "))
#
# b = int(input("Введите 2 число: "))
#
# for i in range(a, b):
#     if i == 7:
#         print(i)
#

# Задача 6

# a = int(input("Введите 1 число: "))
#
# b = int(input("Введите 2 число: "))
#
# for i in range(a, b):
#     print(i)
#
# print()
#
# for i in range(b - 1, a - 1, -1):
#     print(i)
#
# print()
#
# for i in range(a, b):
#
#     if i % 7 == 0:
#         print(i)
#
# print()
#
# for i in range(a, b):
#
#     if i % 5 == 0:
#         print(i)


# Задача 7


a = int(input("Введите 1 число: "))

b = int(input("Введите 2 число: "))

for i in range(a, b):

    if i % 3 != 0 and i % 5 != 0:
        print(i)

    if i % 3 == 0 and i % 5 == 0:

        print("Fizz Buzz")

    else:

        if i % 3 == 0:
            print("Fizz")

        if i % 5 == 0:
            print("Buzz")
