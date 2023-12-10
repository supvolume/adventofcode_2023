# AOC 2023 day 5 part 2
# Direct brute force solution. Take too long to find answer

txt = open("input_day05.txt", 'r').read()
txt_list = list(txt.split("\n\n"))

seed = txt_list[0].split(" ")[1:]
seed_soil = txt_list[1].split("\n")[1:]
soil_fer = txt_list[2].split("\n")[1:]
fer_water = txt_list[3].split("\n")[1:]
water_light = txt_list[4].split("\n")[1:]
light_temp = txt_list[5].split("\n")[1:]
temp_humid = txt_list[6].split("\n")[1:]
humid_lo = txt_list[7].split("\n")[1:]

almanac_list = [seed_soil, soil_fer, fer_water, water_light, light_temp, temp_humid, humid_lo]


def convert_range (given_num, dest, start, range_l):
    if given_num >= start and given_num <= start+range_l-1:
        return dest+given_num-start
    else:
        return False


dest_now = 0    # Current starting input for each almanac
dest_found = False
lowest_lo = 99999999999


# Get seed range
for i in range(int(len(seed)/2)):
    for j in range(int(seed[(i*2)+1])):   # j is each number in the given range

        dest_now = int(seed[i*2])+j     # Each seed
        for almanac in almanac_list:
            for line in almanac:
                dest, source, leng = line.split(" ")
                output = convert_range(int(dest_now), int(dest), int(source), int(leng))
                if output != False:
                    dest_found = output
            if dest_found != False:
                dest_now = dest_found
            dest_found = False
            
        # Find the lowest number of location (last output)
        if dest_now < lowest_lo:
            lowest_lo = dest_now
        
print(lowest_lo)

