# Задание 1
# N1 = int(input("N1 = "))
# N2 = int(input("N2 = "))
# S1 = input("S1 = ")
# S2 = input("S1 = ")
#
# combo_str= s1[:n1] + s2[-n2:]
# print(combo_str)


# Задание  2
# C = input("C = ")
# S = input("S = ")
# S0 = input("S0 = ")
#
# for char in S:
#     if char == c:
#         print(S0, end="")
#     print(char, end="")


# Задание  3

# s = input("s = ")
# s0 = input("s0 = ")
# if s0 not in s:
#     print(s)
# else:
#     found = False
#     for char in s:
#         if char == s0 and not found:
#             found = True
#             continue
#         print(char, end="")


# Задание  4

s = input("s = ")
s1 = input("s1 = ")
s2 = input("s2 = ")

main_index = 0
for index in range(len(s)):
    if s[index] == s1:
        main_index = index

for index in range(len(s)):
    if index == main_index:
        print(s2, end="")
        continue
    print(s[index], end="")
