import os
with open("folder/file.txt") as file:
    text = file.readlines()
    print(text)

    new_list = []
    for line in text:
        if len(line) > 1:
            new_list.append(line)
    print(new_list)
