import random
import time





orange = {"gold":50,"points":0,"damage":0}
blue = {"gold":50,"points":0,"damage":0}
yellow = {"gold":50,"points":0,"damage":0}
red = {"gold":50,"points":0,"damage":0}

sides = [orange,blue,yellow,red]

round_gold = 50

units = {"soldier":{"cost":5,"damage":5},
        "spearman":{"cost":10,"damage":20},
        "shilder":{"cost":20,"damage":40},
        "archer":{"cost":30,"damage":60},
        "magician":{"cost":40,"damage":100}
        }

unit = []

def troops_choice(side):

    troop_damage = []
    troop_list = []
    t = 10

    for i in units:
        unit.append(i)
    
    while side["gold"] > 0:
        if t >= 0:
            time.sleep(1)
            t -= 1
            choices = random.choice(unit)
            cost = units[choices]["cost"]
            damage = units[choices]["damage"]
            if side["gold"] >= cost:
                side["gold"] -= cost
                troop_list.append(choices)
                troop_damage.append(damage)
                side["damage"] = sum(troop_damage)
                print(f"Troop list: {troop_list}")
                print(side["gold"])
                continue
            
        else:
            fight()
            break
    return t


def fight():
    print("fight")


def main():
    
    o_time = troops_choice(orange)
    if orange["gold"] > 0 and o_time > 0:
        troops_choice(orange)
    r_time = troops_choice(red)
    if red["gold"] > 0  and r_time > 0:
        troops_choice(red)
    b_time = troops_choice(blue)
    if blue["gold"] > 0  and b_time > 0:
        troops_choice(blue)
    y_time = troops_choice(yellow)
    if yellow["gold"] > 0  and y_time > 0:
        troops_choice(yellow)




main()
print(orange["damage"])
print(orange["gold"])
print(red["damage"])
print(red["gold"])
print(blue["damage"])
print(blue["gold"])
print(yellow["damage"])
print(yellow["gold"])