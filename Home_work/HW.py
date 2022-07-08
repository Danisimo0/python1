import re
from collections import Counter
import string
#
# s = input("S = ")
# ss = re.search(r'.*?\s(.+)\s\.*\b', s)
# print(ss.group(1) if ss else print(" "))

# Задание 2

# str = input("str = ")
#
# print(len(str.replace(' ', '')))
#

# Задание 3


s = input("str = ")
s_new = ''
# total_occurrences = s.count(s_new)
for i in range(len(s)):

    if s_new.find(s[i]) == -1 and s[i] != ' ':
        s_new += s[i]


        # s_new.counter()
        # s_new.count(s)   Он вернет, сколько раз значение появляется в данной строке.не подходит сама функция (
    # sum([i.strip(string.punctuation).isalpha() for i in s_new.split()])


#
# print(counter(s_new))
#  Логика была такой: Удалить повторяющие буквы, после чего удаленные буквы посчитать, не нашел такой функции,
#  как я понял после цикла, уже снаруже мне нужно возвести переменную с функцией которая уже будет считать
#  то есть алгоритм такой: удаляются повторяющие буквы, после данной функции возвести новую которая оставшие буквы
#  уже посчитает, напишите пожалуйста коменнтарий как можно было сделать . 