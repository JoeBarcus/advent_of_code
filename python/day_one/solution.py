my_list = []
with open('input.txt', 'r') as input_data:
    my_list.append(input_data.readlines())
    input_data.close()

inner_list = my_list[0]

sum_list = []
totals = []
for i in range(len(inner_list)):
    if inner_list[i] != '\n':
        sum_list.append(int(inner_list[i]))
    else:
        totals.append(sum(sum_list))
        sum_list = []

max_one = max(totals)
index_one = totals.index(max_one)
totals.pop(index_one)

max_two = max(totals)
index_two = totals.index(max_two)
totals.pop(index_two)

max_three = max(totals)
index_three = totals.index(max_three)

print(max_one + max_two + max_three)