# AOC 2023 day 8 part 2
import math

txt = open("input_day08.txt", 'r').read()
txt = txt.replace(" ","")
txt_list = list(txt.split("\n\n"))

instruction = txt_list[0]
nodes_list = txt_list[1].split("\n")

# Find all step that end with "A"
start_nodes = []
for i in nodes_list:
    if i[2]=="A":
        start_nodes.append(i[:3])

# Transform to dict
node_dict = {}
for i in nodes_list:
    node_dict[i[:3]] = [i[5:8], i[9:12]]
    
# Find next step
def next_move(node, go):
    if go == "L":
        return node_dict[node][0]
    else:
        return node_dict[node][1]

all_steps = []

for start_node in start_nodes:
    steps = 0
    zzz_found = False
    current_node = start_node
    
    while not zzz_found:
        for direction in instruction:
            current_node = next_move(current_node, direction)
            if current_node[-1] != "Z":
                steps += 1
            else:
                zzz_found = True
    all_steps.append(steps+1)

least_step = all_steps[0]
for i in all_steps[1:]:
    least_step = math.lcm(least_step,i)
print(least_step)