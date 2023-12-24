# AOC 2023 day 8 part 1

txt = open("input_day08.txt", 'r').read()
txt = txt.replace(" ","")
txt_list = list(txt.split("\n\n"))

instruction = txt_list[0]
nodes_list = txt_list[1].split("\n")

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

steps = 0
zzz_found = False
current_node = "AAA"

while not zzz_found:
    for direction in instruction:
        current_node = next_move(current_node, direction)
        if current_node != "ZZZ":
            steps += 1
        else:
            zzz_found = True
print(steps+1)