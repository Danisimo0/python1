def function():
    return print(f"“Don't compare yourself with anyone in this world…"
                 f"\nif you do so, you are insulting yourself.”"
                 f"\nBill Gates")


# function()


# exercise 5

def chetnie(a, b):
    if a == b:
        return "введенл неверно."
    if a > b:
        a, b = b, a
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(int(i), end=' ')


# print('Четные:\n')
# chetnie(1, 25)


# function2(1, 22)


# exercise 6

# def square(a, b, c):
#     d = b * a
#     if not c:
#         e = b + " " * (a - 2) + b
#     else:
#         e = d
#     print(d)
#     for i in range(a - 2):
#         print(e)
#     print(d)
# square(5, "^", True)
# print("")
# square(5, "$", False)


# exercise 7

def retwern(a, b, c, d, e):
    return min(a, b, c, d, e)


# print('\n\nМинимальное:\n', retwern(5,41,4231,13,34))


# exercise 8

def proizvedenie(a, b):
    if a == b:
        return "введенo неверно."
    if a > b:
        a, b = b, a
    res = 1
    for i in range(a, b + 1):
        res *= i
    return res


#
# print("Произведение чисел = ", proizvedenie(2, 5))
#


# exercise 9


def amount_number(x):
    res = 0
    for i in range(len(str(x))):
        res += 1
    return res


# print("Количество цифр  = ", amount_number(1231456))


# exercise 10


def polindrom(x):
    comp = ''.join(reversed(str(x)))
    return str(x) == str(comp)


num = 101
if polindrom(num):
    print("Число ", num, " полиндром.")
else:
    print("Число ", num, " не полиндром.")

# все скачал но еще не актировал ( не запустил )