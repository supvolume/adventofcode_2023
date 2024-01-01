# AOC 2023 day 10 part 1

txt = open("input_day10.txt", 'r').read()
txt_list = list(txt.split("\n"))

# Change the pipe visual to direction of pipe ends (NEWS)
# Eg "|" ends are at North and South, so "|" become "NS"
pipe_loc = {}
for row in range(len(txt_list)):
    for col in range(len(txt_list[row])):
        if txt_list[row][col] == "|":
            pipe_loc[(row,col)] = "NS"
        elif txt_list[row][col] == "-":
            pipe_loc[(row,col)] = "WE"
        elif txt_list[row][col] == "L":
            pipe_loc[(row,col)] = "NE"
        elif txt_list[row][col] == "J":
            pipe_loc[(row,col)] = "NW"
        elif txt_list[row][col] == "7":
            pipe_loc[(row,col)] = "SW"
        elif txt_list[row][col] == "F":
            pipe_loc[(row,col)] = "SE"
        elif txt_list[row][col] == "S":
            pipe_loc[(row,col)] = "NSWE"
        else:
            pipe_loc[(row,col)] = "."

opposite = {"N":"S","S":"N","W":"E","E":"W"}
move = {"N":(-1,0), "S":(1,0), "W":(0,-1),"E":(0,1)}
# Starting pipe        
start_p = [i for i in pipe_loc if pipe_loc[i]=="NSWE"][0]

# Find pipe surounding starting position (S)
# Starting position should have 2 pipes connecting to it,
# but it didn't matter which pipe we choose to start first.

# Map the end and the next pipe end, then use another end as the next focus value
# Eg "-" which is "WE" and we focus on "E", the next pipe should contain 
# the opposite of "E" which is "W" such as "SW",
# which means the next focus is "S" since "W" is already connected
next_pipe = ""
next_lo = ""
for i in "NSWE":
    next_temp = pipe_loc[(start_p[0]+move[i][0], start_p[1]+move[i][1])]
    if opposite[i] in next_temp:
        next_pipe = opposite[next_temp.replace(i,"")]
        next_lo = (start_p[0]+move[i][0], start_p[1]+move[i][1])


count = 1
while len(next_pipe) == 1:  # because S next_lo will be 3 (eg NSW, SWE, etc)
    next_temp = pipe_loc[(next_lo[0]+move[next_pipe][0], next_lo[1]+move[next_pipe][1])]
    next_lo = (next_lo[0]+move[next_pipe][0], next_lo[1]+move[next_pipe][1])    
    next_pipe = next_temp.replace(opposite[next_pipe],"")
    count += 1


print(int(count/2))

