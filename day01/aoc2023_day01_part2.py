# AOC 2023 Part 2
# Note: oneight = 18
import re

txt = open("input_day01.txt", 'r').read()
txt_list = list(txt.split("\n"))

num_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


num_txt_list = []
for i in txt_list:
    found_num = True
    while found_num:
        txt_s = re.search("one|two|three|four|five|six|seven|eight|nine",i)
        if txt_s == None:
            found_num = False
        elif txt_s.group(0) == "one":
            i = i.replace(txt_s.group(0),"1e")
        elif txt_s.group(0) == "two":
            i = i.replace(txt_s.group(0),"2o")
        elif txt_s.group(0) == "three":
            i = i.replace(txt_s.group(0),"3e")
        elif txt_s.group(0) == "four":
            i = i.replace(txt_s.group(0),"4")
        elif txt_s.group(0) == "five":
            i = i.replace(txt_s.group(0),"5e")
        elif txt_s.group(0) == "six":
            i = i.replace(txt_s.group(0),"6")
        elif txt_s.group(0) == "seven":
            i = i.replace(txt_s.group(0),"7n")
        elif txt_s.group(0) == "eight":
            i = i.replace(txt_s.group(0),"8t")
        elif txt_s.group(0) == "nine":
            i = i.replace(txt_s.group(0),"9e")
    num_txt_list.append(i)
        

cal_values = []
for line in num_txt_list:
    all_num = ""
    for i in line:
        if i.isnumeric():
            all_num += i
    cal_values.append(int(all_num[0]+all_num[-1]))

print(sum(cal_values))
