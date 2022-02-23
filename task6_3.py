import os

all_files = os.listdir()
file_dict = {}

for file_name in all_files:
    if '.txt' in file_name:
        with open(file_name, encoding='utf-8') as read_list:
            file_dict[file_name] = read_list.readlines()
            # print(file_dict)


def get_key(value):
    for k, v in file_dict.items():
        if v == value:
            return k


with open('sorted_file.txt', 'a', encoding='utf-8') as new_file:
    sorted_list = sorted(file_dict.values(), key=lambda x: len(x), reverse=False)
    # print(sorted_list)
    for line in sorted_list:
        new_file.write(get_key(line))
        new_file.write('\n')
        new_file.write(str(len(line)))
        new_file.write('\n')
        new_file.write(str(''.join(line)))
        new_file.write('\n')
        # new_file.write(str('\n'.join(line)))
