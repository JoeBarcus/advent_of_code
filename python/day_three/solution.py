import string

letters_map = list(string.ascii_lowercase) + list(string.ascii_uppercase)
numbers_map = list(range(1, 53))
result_map = dict(zip(letters_map, numbers_map))

with open('input.txt', 'r') as input_data:
    rucksack_data = input_data.read().split('\n')
    input_data.close()

split_rucksacks = []
for item in rucksack_data:
    midpoint = int(len(item) / 2)
    first = item[0:midpoint]
    second = item[midpoint: int(len(item))]
    rucksacks = (first, second)
    split_rucksacks.append(rucksacks)

def find_similar_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    similar_characters = set1.intersection(set2)

    return ''.join(similar_characters)

similar_char_list = []
for ruck in split_rucksacks:
    similar_chars = find_similar_characters(ruck[0], ruck[1])
    mapped_value = result_map.get(similar_chars)
    similar_char_list.append(mapped_value)

print(sum(similar_char_list))


##############  Part 2  ##############


letter_list = []
for i in range(0, len(rucksack_data), 3):
    three_items = rucksack_data[i:i + 3]
    three_sets = [set(string) for string in three_items]

    common_letter = set.intersection(*three_sets)
    letter_list.append(common_letter)

letter_list_converted = [''.join(letters) for letters in letter_list]

mapped_values = [result_map[item] for item in letter_list_converted]

print(sum(mapped_values))

