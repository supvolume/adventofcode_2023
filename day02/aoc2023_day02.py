# AOC 2023 day 2
txt = open("input_day02.txt", 'r').read()
txt_list = list(txt.split("\n"))

# Part 1 Condition
# if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
max_red = 12
max_green = 13
max_blue = 14

game_fit_cond = [] # for part 1
min_power = [] # for part 2

for game in txt_list:
    game_num_set = game.split(": ")
    game_num = int(game_num_set[0].split(" ")[1])
    cube_set = game_num_set[1].split("; ")

    # To find max possibility of part 1
    red = 0
    green = 0
    blue = 0
    
    # Each set in the game
    for cs in cube_set:
        cube = cs.split(", ")

        # Each cube in the set
        for c in cube:
            c_sep = c.split(" ")
            if c_sep[1] == "red":
                if int(c_sep[0]) > red:
                    red = int(c_sep[0])
            if c_sep[1] == "green":
                if int(c_sep[0]) > green:
                    green = int(c_sep[0])
            if c_sep[1] == "blue":
                if int(c_sep[0]) > blue:
                    blue = int(c_sep[0])

    # check if condition fit (part 1)
    if (red <= max_red) and (green <= max_green) and (blue <= max_blue):
        game_fit_cond.append(game_num)

    # find power in part 2
    min_power.append(red*green*blue)

print("Part 1: ", str(sum(game_fit_cond)))
print("Part 2: ", str(sum(min_power)))
