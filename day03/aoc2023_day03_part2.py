# AOC 2023 day 3 part 2
txt = open("input_day03.txt", 'r').read()
txt_list = list(txt.split("\n"))

# Find "*" surrounding locations
sym_lo = {}
for i in range(len(txt_list)):
    for j in range(len(txt_list[i])):
        if txt_list[i][j] == "*":
            sym_lo[(i,j)] =[(i-1,j-1),
                           (i-1,j),
                           (i-1,j+1),
                           (i,j-1),
                           (i,j+1),
                           (i+1,j-1),
                           (i+1,j),
                           (i+1,j+1)]

# Check if the number is the part number
part_num_dict = {}
part_num = ""
near_sym = False
check_lo = ""  # identify the current * that are being check

for i in range(len(txt_list)):
    for j in range(len(txt_list[i])):
        if txt_list[i][j].isnumeric():
            part_num += txt_list[i][j]
            
            # Check if the number is near "*" location or not
            for k, v in sym_lo.items():
                if ((i,j) in v) and not near_sym:
                    near_sym = True
                    check_lo = k
                
        # End of number
        else:
            if part_num.isnumeric() and near_sym:
                if check_lo in part_num_dict:
                    part_num_dict[check_lo].append(int(part_num))
                else:
                    part_num_dict[check_lo] = [int(part_num)]
            part_num = ""
            near_sym = False

# Check which "*" is connect to 2 numbers (2 gears)
part_num_list = []
for v in part_num_dict.values():
    if len(v) == 2:
        part_num_list.append(v[0]*v[1])

print(sum(part_num_list))
