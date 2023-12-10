# AOC 2023 day 6 part 2
#button_time = speed = from 0 to record_time
#distance = button_time*(record_time-button_time)

txt = open("input_day06.txt", 'r').read()
txt = txt.replace(" ","")
txt_list = list(txt.split("\n"))


record_time = int(txt_list[0].split(":")[1])
record_distance = int(txt_list[1].split(":")[1])

win_way = []

count = record_time
win_button_time = []

# Find the less and most possible time to win the race by
# check if button time are able to win the race alternate from min and max
for j in range(1, (record_time//2)+2):
    distance_b_min = j*(record_time-j)
    distance_b_max = count*(record_time-count)
    if distance_b_min > record_distance:
        win_button_time.append(j)
    if distance_b_max > record_distance:
        win_button_time.append(count)
    count -= 1

    # Find the number of time between less and most possible race win time
    if len(win_button_time) >= 2:
        win_way.append(max(win_button_time)-min(win_button_time)+1)
        break

multiply_way = 1
for i in win_way:
    multiply_way *= i

print(multiply_way)
