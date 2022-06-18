import os
with open("folder/file.txt") as file:
    text = file.readlines()
    print(text)

    new_list = []
    for line in text:
        if len(line) > 1:
            new_list.append(line)
    print(new_list)

try:
    os.mkdir("folder/new")
except:
    print("folder already created")

    for i in range(0, len(new_list)):
        file_name = f'folder/new/file{i}.txt'
        with open(file_name, 'w') as f:
            f.write(new_list[i])
    os.remove("folder/file.txt")