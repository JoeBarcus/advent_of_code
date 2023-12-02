with open ('input.txt', 'r') as input_data:
    directories = input_data.read().split('\n')
    input_data.close()

directory_dict = {}
full_path = ""
total_size = 0
list_len = len(directories)

for command in directories:

    current_idx = directories.index(command)        

    if str.split(command)[0].isdigit():
        total_size += int(str.split(command)[0])

    if list_len - current_idx == 1:
        directory_dict[full_path] = total_size

    if '$ cd' in command and '/' not in command:
        
        if '/' not in command and '..' not in command:
            if full_path not in directory_dict.keys():
                directory_dict[full_path] = total_size
            full_path += '/' + str.split(command, ' ')[2]

        if '..' in command:           
            if full_path not in directory_dict.keys():
                directory_dict[full_path] = total_size
            path_list = str.split(full_path, '/')
            full_path = '/'.join(path_list[:-1])
            if full_path in directory_dict.keys():
                current_total = directory_dict[full_path]
                directory_dict[full_path] = current_total + total_size         
        
        total_size = 0

at_most = 100000

d = {k: v for (k, v) in directory_dict.items() if v <= at_most}

print(sum(d.values()))

minimum_delete_size = 70_000_000 - directory_dict['']
print(directory_dict)

e = {k: v for (k, v) in directory_dict.items() if v >= minimum_delete_size}

print(sum(e.values()))
