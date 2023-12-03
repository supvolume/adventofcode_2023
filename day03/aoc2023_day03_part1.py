# AOC 2023 day 3 part 1
txt = open("input_day03_test.txt", 'r').read()
txt_list = list(txt.split("\n"))

# Find symbol surrounding locations
sym_lo = []
for i in range(len(txt_list)):
    for j in range(len(txt_list[i])):
        if (not txt_list[i][j].isnumeric()) and (txt_list[i][j] != "."):
            sym_lo.extend(((i-1,j-1),
                           (i-1,j),
                           (i-1,j+1),
                           (i,j-1),
                           (i,j+1),
                           (i+1,j-1),
                           (i+1,j),
                           (i+1,j+1)))

part_num_list = []
part_num = ""
near_sym = False
# Check if the number is the part number
for i in range(len(txt_list)):
    for j in range(len(txt_list[i])):
        if txt_list[i][j].isnumeric():
            part_num += txt_list[i][j]
            
            # Check if the number is near symbol location or not
            if (i,j) in sym_lo:
                near_sym = True
                
        # End of number
        else:
            if part_num.isnumeric() and near_sym:
                part_num_list.append(int(part_num))
            part_num = ""
            near_sym = False
print(sum(part_num_list))
