from collections import deque

with open('input.txt', 'r') as input_data:
    crates = input_data.read().split('\n')
    input_data.close()

for i, crate in enumerate(crates):
    if crate == '':
        index_of_input = i

initial_crate_state = crates[0: index_of_input]

crate_moves = crates[index_of_input + 1: ]

d_one = deque()
d_two = deque()
d_three = deque()
d_four = deque()
d_five = deque()
d_six = deque()
d_seven = deque()
d_eight = deque()
d_nine = deque()

for crate in initial_crate_state:
    if crate[1].isalpha():
        d_one.append(crate[1])
    if crate[5].isalpha():
        d_two.append(crate[5])
    if crate[9].isalpha():
        d_three.append(crate[9])
    if crate[13].isalpha():
        d_four.append(crate[13])
    if crate[17].isalpha():
        d_five.append(crate[17])
    if crate[21].isalpha():
        d_six.append(crate[21])
    if crate[25].isalpha():
        d_seven.append(crate[25])
    if crate[29].isalpha():
        d_eight.append(crate[29])
    if crate[33].isalpha():
        d_nine.append(crate[33])    

# Left is top on each deque.  Right is the bottom.

deque_mappings = {
    1: d_one,
    2: d_two,
    3: d_three,
    4: d_four,
    5: d_five,
    6: d_six,
    7: d_seven,
    8: d_eight,
    9: d_nine,
}

# for move in crate_moves:
#     parts = move.split(' ')
#     quantity = int(parts[1])
#     d_from = int(parts[3])
#     d_to = int(parts[5])
#     for qty in range(quantity):
#         deque_mappings.get(d_to).appendleft(deque_mappings.get(d_from).popleft())
        

# for deq in deque_mappings:
#     print(deque_mappings.get(deq)[0])


###########  Part 2  ###########


for move in crate_moves:
    popped_list = []
    parts = move.split(' ')
    quantity = int(parts[1])
    d_from = int(parts[3])
    d_to = int(parts[5])
    for qty in range(quantity):
        popped_list.append(deque_mappings.get(d_from).popleft())
    print(popped_list)
    popped_list.reverse()
    for popped in popped_list:
        deque_mappings.get(d_to).appendleft(popped)

for deq in deque_mappings:
    print(deque_mappings.get(deq)[0])