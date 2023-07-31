
with open('input.txt', 'r') as input_data:
    camp_cleanup = input_data.read().split('\n')
    input_data.close()

#print(camp_cleanup)

overlap = 0
for camp in camp_cleanup:
    split_camp = camp.split(',')
    split_camp_one = split_camp[0].split('-')
    split_camp_one = [int(num) for num in split_camp_one]
    split_camp_two = split_camp[1].split('-')
    split_camp_two = [int(num) for num in split_camp_two]

    if split_camp_one[0] >= split_camp_two[0] and split_camp_one[1] <= split_camp_two[1]:
        overlap += 1
    elif split_camp_two[0] >= split_camp_one[0] and split_camp_two[1] <= split_camp_one[1]:
        overlap += 1

print(overlap)
