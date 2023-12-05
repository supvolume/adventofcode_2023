# AOC 2023 day 4 part 2
txt = open("input_day04.txt", 'r').read()
txt_list = list(txt.split("\n"))

tot_card = 0
card_n = len(txt_list)
    
for c in txt_list:
    [card, numbers] = c.split(": ")
    [win_num, your_num] = numbers.split(" | ")
    win_num = win_num.split(" ")
    your_num = your_num.split(" ")

    # Remove empty string
    win_num = [x for x in win_num if x != ""]
    your_num = [x for x in your_num if x != ""]

    card_point = len(set(your_num).intersection(set(win_num)))
    if card_point != 0:
        for i in range(card_point):
            if i+1 <= card_n:
                txt_list.append(txt_list[int(card.split(" ")[-1])+i])

print(len(txt_list))
    
