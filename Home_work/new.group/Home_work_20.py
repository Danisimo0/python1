from functools import reduce


# fib1 = 1
# fib2 = 1
# n = input("Номер элемента : ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("Значение этого элемента:", fib2)


# Задача 2

# пытался с инпутом, много перепробовал, не получилось


# !~!~!~!~!~!~!~!~!~!~!~!~!~
# num = lambda x: x*3
# print(num(5))

# Задача 3

# x = input("x = ")
#
# even = 0
# odd = 0
#
# for i in x:
#     if int(i) % 2 == 0:
#         even *= 2
#     else:
#         odd *= 2
#
# print("Even: %d, odd: %d" % (even, odd))


# Задача 4
# def multiply2(x):
#     return x * 2
#
#
# mi = map(multiply2, [0, -5, 12, 36, -12])
# print(mi)
# numbers = [0, -5, 12, 36, -12]
# new_list = list(map(lambda x: x*2 , numbers))
# print(new_list)

# Задача 5

# newlist = list(filter(lambda n: n > 0 , [0, -5, 12, 5, -31, 36, 9, -12, 4, 3]))
# print(sum(rangenewlist))

# Задача 6


# list = [0, -5, 12, 5, -31, 36, 9, -12, 4, 3]
# list2 = []
# # list2 = reduce(lambda x: x*2 ,list) не получилось
#
# for number in list:
#
#     if number >= 0:
#         list2.append(number)
# print(sum(list2))
