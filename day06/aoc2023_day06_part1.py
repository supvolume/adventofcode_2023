# AOC 2023 day 6 part 1
#button_time = speed = from 0 to record_time
#distance = button_time*(record_time-button_time)

txt = open("input_day06.txt", 'r').read()
txt_list = list(txt.split("\n"))

time = list(filter(lambda x: x != "", txt_list[0].split(" ")))[1:]
dist = list(filter(lambda x: x != "", txt_list[1].split(" ")))[1:]

time = [int(x) for x in time]
dist = [int(x) for x in dist]


win_way = []

for i in range(len(time)):
    record_time = time[i]
    record_distance = dist[i]
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
