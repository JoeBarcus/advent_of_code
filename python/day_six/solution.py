with open ('input.txt', 'r') as input_data:
    signal_packet = input_data.read()
    input_data.close()

consecutive_counter_set = set()

for i, letter in enumerate(signal_packet):
    if letter in consecutive_counter_set:
        consecutive_counter_set = set()
        continue
    consecutive_counter_set.add(letter)
    
    if len(consecutive_counter_set) == 4:
        packet = i
        break


print(packet)


consecutive_counter_set = set()

for i, letter in enumerate(signal_packet):
    if letter in consecutive_counter_set:
        consecutive_counter_set = set()
        continue
    consecutive_counter_set.add(letter)
    
    if len(consecutive_counter_set) == 14:
        packet = i + 1
        break


print(packet)