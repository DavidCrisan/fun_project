import random
import time





orange = {"gold":50,"points":0}
blue = {"gold":50,"points":0}
yellow = {"gold":50,"points":0}
red = {"gold":50,"points":0}

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
    fail_try = []
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
                print(f"Troop list: {troop_list}")
                print(side["gold"])
                continue
            else:
                fail_try.append(choices)
                print(f"Fail list: {fail_try}")
                print(side["gold"])
                continue
        else:
            main()
            break
    return troop_damage





def main():
    if orange["gold"] > 0:
        orange_damage = troops_choice(orange)
    if red["gold"] > 0:
        red_damage = troops_choice(red)
    if blue["gold"] > 0:
        blue_damage = troops_choice(blue)
    if yellow["gold"] > 0:
        yellow_damage = troops_choice(yellow)

    return orange_damage,red_damage,blue_damage,yellow_damage


orange_damage, red_damage, blue_damage, yellow_damage = main()
orange_bp = sum(orange_damage)
print(orange_bp)
# print(troop_list)
print(orange["gold"])
red_bp = sum(red_damage)
print(red_bp)
# print(troop_list)
print(red["gold"])
blue_bp = sum(blue_damage)
print(blue_bp)
# print(troop_list)
print(blue["gold"])
yellow_bp = sum(yellow_damage)
print(yellow_bp)
# print(troop_list)
print(yellow["gold"])