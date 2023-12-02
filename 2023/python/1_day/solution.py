with open("input.txt", "r") as input_data:
    coordinates = input_data.read().split('\n')
    input_data.close()


# Part 1
total = 0
for coord in coordinates:
    coord_list = [i for i in coord if i.isdigit()]
    total += int(f'{coord_list[0]}{coord_list[-1]}')

print(f'Part 1: {total}')


# Part 2
number_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
number_map_reversed = {k[::-1]: v for k, v in number_map.items()}

def get_first_number(coordinate: str, number_map: dict) -> int:
    string_builder = ''
    for input_keys in coordinate:
        if input_keys.isdigit():
            return input_keys
        string_builder += str(input_keys)
        filtered_dict = {k: v for k, v in number_map.items() if k in string_builder}
        if len(filtered_dict) == 1:
            return list(filtered_dict.values())[0]
        
total = 0
for coord in coordinates:
    left_coord = get_first_number(coord, number_map)
    right_coord = get_first_number(coord[::-1], number_map_reversed)
    total += int(f'{left_coord}{right_coord}')

print(f'Part 2 {total}')