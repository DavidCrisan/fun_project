import random
import time
import sys





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
        if t > 0:
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
            break
    return t


def status():

    print(f"Orange damage: {orange['damage']}")
    print(f'Orange gold left: {orange["gold"]}')
    
    print(f"Red damage: {red['damage']}")
    print(f'Red gold left: {red["gold"]}')
        
    print(f"Blue damage: {blue['damage']}")
    print(f'Blue gold left: {blue["gold"]}')
        
    print(f"Yellow damage: {yellow['damage']}")
    print(f'Yellow gold left: {yellow["gold"]}')
    time.sleep(5)



def fight():
    status()

    winner()

def winner():

    winning = False

    if orange["points"] == 5:
        print("Orange is the winner")
        sys.exit()
    if blue["points"] == 5:
        print("Blue is the winner")
        sys.exit()
    if red["points"] == 5:
        print("Red is the winner")
        sys.exit()
    if yellow["points"] == 5:
        print("Yellow is the winner")
        sys.exit()
    else:
        restart()

    return winning

def restart():
    blue["gold"] += 50
    red["gold"] += 50
    yellow["gold"] += 50
    orange["gold"] += 50
    
    blue["damage"] = 0
    red["damage"] = 0
    yellow["damage"] = 0
    orange["damage"] = 0

    main()




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




winning = winner()

while winning == False:
    fight()

