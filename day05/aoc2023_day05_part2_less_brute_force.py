# AOC 2023 day 5 part 2
# Backward brute force solution.
# Running location number starting from 0 until it find matching seed number

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

almanac_list = [humid_lo,
                temp_humid,
                light_temp,
                water_light,
                fer_water,
                soil_fer,
                seed_soil]

def convert_range (given_num, dest, start, range_l):
    if dest <= given_num <= dest+range_l-1:
        return start+given_num-dest
    else:
        return False

# Create seed range
seed_range = []
for i in range(int(len(seed)/2)):
    seed_range.append((int(seed[(i*2)]),(int(seed[(i*2)])+int(seed[(i*2)+1])-1)))

# Find the lowest location that in a given seed range
start_now = 0
seed_found = False
almanac_start_found = False


for i in range(0,9999999999):   # i is current location number
    start_now = i
    for almanac in almanac_list:
        for line in almanac:
            dest, source, leng = line.split(" ")
            output = convert_range(start_now,
                                   int(dest),
                                   int(source),
                                   int(leng))
            if output != False:
                almanac_start_found = output
        if almanac_start_found != False:
            start_now = almanac_start_found
        almanac_start_found = False
    #print("location: ", str(i))
    #print(start_now)
    #print("\n")
    # Check if current location number is in seed list
    if any(lower <= start_now <= upper for (lower, upper) in seed_range):
        print(i)
        break
           

"""
dest_now = 0    # Current starting input for each almanac
dest_found = False


    


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

"""
