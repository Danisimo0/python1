# some_str = input("some str: ")
# if some_str.count(" ") == 1:
#     print("only 1 space")
# else:
#     first_space_index = some_str.find(" ")
#     second_space_index = some_str[first_space_index+1:].find(" ")
#     print(some_str[first_space_index+1:first_space_index+second_space_index+1])

# Задание 2

# words = input("sentence: ").split()
# summa = 0
# for word in words:
#      summa += len(word)
# print(summa / len(words))

# Задание 3

words = input("sentence: ").split()
counter = 0

for word in words:
    unique_chars = 0
    word = word.lower()
    for char in word:
        if word.count(char) == 1:
            unique_chars += 1
    if len(word) == unique_chars:
        counter += 1

print(counter)
