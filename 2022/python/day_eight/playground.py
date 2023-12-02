with open('input.txt') as input_data:
    forest = input_data.read().split('\n')
    input_data.close()


forest_list = [[*x] for x in forest]

transposed = list(map(list, zip(*forest_list)))

transposed_joined_forest_list = [''.join(t) for t in transposed]

