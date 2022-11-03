# a = 10.2
# b = "Python"
# print(f"{a}{b}")

# print()


# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# txt2 = "My name is {0}, I'm {1}".format("John",36)
# txt3 = "My name is {}, I'm {}".format("John",36)
# txt4 = "Version is {1}, {0}".format(10.2, "Python")
# print(txt4)

# import math

# print(math.sqrt(25))

# list1 = {"name": "Danil", "age": 22, "id": 2}

# print(list1["age"])


# class Vech:
#     def has_bag(self):
#         return True
#
#
# teh1 = Vech()
# # print(type(teh1))
# print(teh1.has_bag())
#
#
# class Car(Vech):
#     def has_bag(self):
#         return False
#
#
# myCar = Car()
# print(myCar.has_bag())


# a = 1
# while a >=0:
#     print(f'{a}')
#     a = a+1
#     if a >10:
#         break


# list_2 = [1, 2, 3, 4, 5, True]
# for i in list_2:
#     print(i)
# newlist = [x for x in range(1, 5+1) if x % 2 == 0]
# print(newlist)
# import os
#
# p = os.path.abspath()
# print(p)
#

# def add_four_value(func):
#     def vrapper(*args, **kwargs):
#         greeting = func(*args, **kwargs)
#         return greeting+10
#
#     return vrapper
#
#
# @add_four_value
# def sum_three_value(var1, var2, var3) -> float:
#     return var1 + var2 + var3
#
#
# res = sum_three_value(10, 20, 30)
# print(res)


# a = lambda b, c: b  c
# print(a(5, 10))
import math
a = lambda i: math.sqrt(i)
print(a(-9))