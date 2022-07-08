# Задание 1
# n1 = int(input("N1 = "))
# n2 = int(input("N2 = "))
# s1 = input("S1 = ")
# s2 = input("S2 = ")
# print(s1[:n1] + s2[-n2:])
#
#
# print("\n\n\n*********************************\n\n\n")
#
# c = input("c = ")
# s = input("s = ")
# s0 = input("s0 = ")
#
# for char in s:
#     if char == c:
#         print(s0, end="")
#     print(char, end="")


# print("\n\n\n*********************************\n\n\n")

# s = input("s =")
# s0 = input("s0 = ")
# if s0 not in s:
#     print(s)
# else:
#     found = False
#     for char in s:
#         if char in s:
#             if char in s:
#                 found = True
#                 continue
#             print(char, end="")

# print("\n\n\n*********************************\n\n\n")

s = input("s = ")
s1 = input("s1 = ")
s2 = input("s2 = ")
last_index = 0
for index in range(len(s)):
    if s[index] == s1:
        last_index = index

for index in range(len(s)):
    if index == last_index:
        print(s2)
        continue
    print(s[index])
