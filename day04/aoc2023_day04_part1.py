# AOC 2023 day 4 part 1
txt = open("input_day04.txt", 'r').read()
txt_list = list(txt.split("\n"))

point = 0

for c in txt_list:
    [card, numbers] = c.split(": ")
    [win_num, your_num] = numbers.split(" | ")
    win_num = win_num.split(" ")
    your_num = your_num.split(" ")

    # Remove empty string
    win_num = [x for x in win_num if x != ""]
    your_num = [x for x in your_num if x != ""]
    
    card_point = len(set(your_num).intersection(set(win_num)))
    

    # Calculate score for each card
    if card_point > 0:
        point += (2**(card_point-1))

print(point)
