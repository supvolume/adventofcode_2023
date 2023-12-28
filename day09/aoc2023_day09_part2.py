# AOC 2023 day 9 part 2

txt = open("input_day09.txt", 'r').read()
txt_list = list(txt.split("\n"))

history_list = []
for i in txt_list:
    history_list.append(list(int(j) for j in i.split(" ")))

#Recursion until the final list contain 0 only
def prediction(value_list):
    if all(i==0 for i in value_list):
        return 0
    else:
        temp_list = []
        for i in range(len(value_list)-1):
            temp_list.append(value_list[i+1]-value_list[i])        
        return value_list[0] - prediction(temp_list)
    
all_predict = []
for history in history_list:
    all_predict.append(prediction(history))

print(sum(all_predict))

