import numpy as np

with open('input.txt') as input_data:
    forest = input_data.read().split('\n')
    input_data.close()



forest_list = [[x] for x in forest]

array = np.array(forest_list)

print(len(array))

print(len(array[0]))

print(array[0])













# can_be_seen = []

# for i in forest_list:

#     horizontal_check = i[0]
#     for count, value in enumerate(horizontal_check):
#         value = int(value)
#         if count == 0:
#             can_be_seen.append(value)
#             print(f'count = {count} left {value}')
#             continue
#         elif value <= int(horizontal_check[count-1]):
#             break
#         else:
#             can_be_seen.append(value)
#             print(f'count else left  {value}')

#     horizontal_check_reverse = horizontal_check[::-1]
#     for count, value in enumerate(horizontal_check):
#         value = int(value)  
#         if count == 0:
#             can_be_seen.append(value)
#             print(f'count = {count} right {value}')
#             continue
#         elif value <= int(horizontal_check[count-1]):
#             break
#         else:
#             can_be_seen.append(value)
#             print(f'{count} else right {value}')

# forest_list = [[*x] for x in forest]
# transposed = list(map(list, zip(*forest_list)))
# transposed_joined_forest_list = [''.join(t) for t in transposed]

# for i in transposed_joined_forest_list:

#     horizontal_check = i[0]
#     for count, value in enumerate(horizontal_check):
#         value = int(value)
#         if count == 0:
#             can_be_seen.append(value)
#             print(f'count = {count} left transpose {value}')
#             continue
#         elif value < int(horizontal_check[count-1]):
#             break
#         else:
#             can_be_seen.append(value)
#             print(f'{count} else left transpose {value}')

#     horizontal_check_reverse = horizontal_check[::-1]
#     for count, value in enumerate(horizontal_check):
#         value = int(value)  
#         if count == 0:
#             can_be_seen.append(value)
#             print(f'count = {count} right transpose {value}')
#             continue
#         elif value < int(horizontal_check[count-1]):
#             break
#         else:
#             can_be_seen.append(value)
#             print(f'{count} else right transpose {value}')


# print(can_be_seen)
