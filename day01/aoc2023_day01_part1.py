# AOC 2023 Part 1
txt = open("input_day01.txt", 'r').read()
txt_list = list(txt.split("\n"))


cal_values = []
for line in txt_list:
    all_num = ""
    for i in line:
        if i.isnumeric():
            all_num += i
    cal_values.append(int(all_num[0]+all_num[-1]))

print(sum(cal_values))
