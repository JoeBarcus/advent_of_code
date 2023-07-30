elf_plays = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

my_plays = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

my_outcome = {
    'X': 'Lose',
    'Y': 'Tie',
    'Z': 'Win'
}

scoring = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}

winning = {
    'Lose': 0,
    'Tie': 3,
    'Win': 6
}


with open('input.txt', 'r') as input_data:
    rock_paper_scissors_data = input_data.read().split('\n')
    input_data.close()
    
# Code for Part 1
def determine_winner(elf, player):
    elf_pick = elf_plays.get(elf)
    my_pick = my_plays.get(player)

    if elf_pick == my_pick:
        return 'Tie'
    
    elif elf_pick == 'Rock' and my_pick == 'Paper':
        return 'Win'
    
    elif elf_pick == 'Rock' and my_pick == 'Scissors':
        return 'Lose'
    
    elif elf_pick == 'Paper' and my_pick == 'Rock':
        return 'Lose'
    
    elif elf_pick == 'Paper' and my_pick == 'Scissors':
        return 'Win'
    
    elif elf_pick == 'Scissors' and my_pick == 'Paper':
        return 'Lose'
    
    elif elf_pick == 'Scissors' and my_pick == 'Rock':
        return 'Win'
    
grand_totals = []
for i in range(len(rock_paper_scissors_data)):

    elf = rock_paper_scissors_data[i][0]
    player = rock_paper_scissors_data[i][2]
    
    pick_score = scoring.get(my_plays.get(player))

    winning_check = determine_winner(elf, player)
    winning_score = winning.get(winning_check)

    grand_totals.append(pick_score + winning_score)

# Answer to part 1
print(sum(grand_totals))

# Code for Part 2

def what_to_play(elf, outcome):
    if my_outcome.get(outcome) == 'Tie':
        my_play = elf_plays.get(elf)
        return my_play
    
    if my_outcome.get(outcome) == 'Win':
        if elf == 'A':
            return 'Paper'
        elif elf == 'B':
            return 'Scissors'
        else:
            return 'Rock'
            
    if my_outcome.get(outcome) == 'Lose':
        if elf == 'A':
            return 'Scissors'
        elif elf == 'B':
            return 'Rock'
        else:
            return 'Paper'

grand_totals_part_two = []
for i in range(len(rock_paper_scissors_data)):

    # Get the elfs move
    elf = rock_paper_scissors_data[i][0]

    # Get the desired outcome
    outcome = rock_paper_scissors_data[i][2]


    winning_score = winning.get(my_outcome.get(outcome))
    pick = what_to_play(elf, outcome)
    pick_score = scoring.get(pick)
    grand_totals_part_two.append(winning_score + pick_score)

# Answer to Part 2
print(sum(grand_totals_part_two))
    