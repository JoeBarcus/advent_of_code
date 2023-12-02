with open("input.txt", "r") as input_data:
    game_data = input_data.read().split('\n')
    input_data.close()


# Part 1

max_cube_dict = {'red': 12,
                 'green': 13,
                 'blue': 14}


invalid_games = []
for idx, game in enumerate(game_data):
    game_samples = str.split(game, ':')[1]
    game_samples_list = str.split(game_samples, ';')
    for game_samples in game_samples_list:
        score_groups = game_samples.split(',')
        for score in score_groups:
            score = str.split(score.strip(), ' ')
            max_count_check = { k: v for k, v in max_cube_dict.items() if k in score}
            if int(score[0]) > list(max_count_check.values())[0]:
                invalid_games.append(idx + 1)


total_games = list(range(1, len(game_data) + 1))
viable_games = set(total_games) - set(invalid_games)
print(sum(viable_games))


# Part 2

game_power = []
for idx, game in enumerate(game_data):
    game_samples = str.split(game, ':')[1]
    game_samples_list = str.split(game_samples, ';')
    red_max = 0
    blue_max = 0
    green_max = 0
    for game_samples in game_samples_list:
        score_groups = game_samples.split(',')
        for score in score_groups:
            score = str.split(score.strip(), ' ')
            if score[1] == 'green' and int(score[0]) > green_max:
                green_max = int(score[0])
            elif score[1] == 'red' and int(score[0]) > red_max:
                red_max = int(score[0])
            elif score[1] == 'blue' and int(score[0]) > blue_max:
                blue_max = int(score[0])
    game_power.append(red_max * blue_max * green_max)

print(sum(game_power))