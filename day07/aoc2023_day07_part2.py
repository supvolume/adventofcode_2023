# AOC 2023 day 7 part 2
import pandas as pd
from pandas.api.types import CategoricalDtype

txt = open("input_day07.txt", 'r').read()
txt = txt.replace(" ","")
txt_list = list(txt.split("\n"))

def get_face(card):
    face = {}
    for i in card:
        if i not in face:
            face[i] = 1
        else:
            face[i] += 1
            
    # Sort then tuple key, value
    if "J" in face:
        # Five of a kind
        if len(face) <= 2:
            return 7
        else:
            j_value = face["J"]
            del face["J"]
            face = sorted(((v,k) for k,v in face.items()))
            # Four of a kind
            if face[-1][0] + j_value == 4:
                return 6
            # Full house
            elif (face[-1][0] + j_value == 3) and (face[-2][0] == 2):
                return 5
            # Three of a kind
            elif face[-1][0] + j_value == 3:
                return 4
            # Two pair
            elif (face[-1][0] == 2) and (face[-2][0]+j_value == 2):
                return 3
            elif face[-1][0] + j_value == 2:
                return 2
        
    else:
        face = sorted(((v,k) for k,v in face.items()))
        # Five of a kind
        if face[-1][0] == 5:
            return 7
        # Four of a kind
        elif face[-1][0] == 4:
            return 6
        # Full house
        elif (face[-1][0] == 3) and (face[-2][0] == 2):
            return 5
        # Three of a kind
        elif face[-1][0] == 3:
            return 4
        # Two pair
        elif (face[-1][0] == 2) and (face[-2][0] == 2):
            return 3
        # One pair
        elif face[-1][0] == 2:
            return 2
        else:
            return 1

df = pd.DataFrame(txt_list, columns=["card"])
df["bit"] = df["card"].astype(str).str[5:].astype(int)
df["card"] = df["card"].astype(str).str[0:5]
df["c1"] = df["card"].astype(str).str[0]
df["c2"] = df["card"].astype(str).str[1]
df["c3"] = df["card"].astype(str).str[2]
df["c4"] = df["card"].astype(str).str[3]
df["c5"] = df["card"].astype(str).str[4]


df["count_face"] = df["card"].apply(get_face)

card_order = CategoricalDtype(categories=["J","2", "3", "4", "5",
                                          "6", "7", "8", "9", 
                                          "T", "Q", "K", "A"
                                           ], ordered=True)

for i in ["c1","c2","c3","c4","c5"]:
    df[i] = df[i].astype(card_order)

df = df.sort_values(by=["count_face", "c1","c2","c3","c4","c5"]) \
.reset_index()

df["total_win"] = (df.index+1)*df["bit"]
print(sum(df["total_win"]))