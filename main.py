import random
import time
import sys


# Creating the side
orange = {"gold":0,"points":0,"damage":0,"tag":"Orange"}
blue = {"gold":0,"points":0,"damage":0,"tag":"Blue"}
yellow = {"gold":0,"points":0,"damage":0,"tag":"Yellow"}
red = {"gold":0,"points":0,"damage":0,"tag":"Red"}
sides = []

# Creating the units
units = {"soldier":{"cost":5,"damage":5},
        "spearman":{"cost":10,"damage":20},
        "shilder":{"cost":20,"damage":40},
        "archer":{"cost":30,"damage":60},
        "magician":{"cost":40,"damage":100}
        }
unit = []

# Function that randomly choose units for eac sides and calculate their damage
def troops_choice(side):

    troop_damage = []
    troop_list = []
    t = 10

    for i in units:
        unit.append(i)
    
    while side["gold"] > 0:
        if t > 0:
            time.sleep(1)
            t -= 2
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

# Function that prints the status of each side
def status():

    print(f'Orange status. Damage: {orange["damage"]}, gold: {orange["gold"]}, points:{orange["points"]}')
    print(f'Blue status. Damage: {blue["damage"]}, gold: {blue["gold"]}, points:{blue["points"]}')
    print(f'Red status. Damage: {red["damage"]}, gold: {red["gold"]}, points:{red["points"]}')
    print(f'Yellow status. Damage: {yellow["damage"]}, gold: {yellow["gold"]}, points:{yellow["points"]}')
    time.sleep(5)

# Function that randomly choose the opponents, give the gold after each fight and decide the winner of the round
def fight():

    status()
    sides = [orange,blue,yellow,red]

    while len(sides) > 0:
        choice = random.choice(sides)
        sides.remove(choice)
        choice_2 = random.choice(sides)
        sides.remove(choice_2)
        if len(sides) == 2:
            if choice["damage"] > choice_2["damage"]:
                choice["damage"] = choice["damage"] - choice_2["damage"]
                choice_2["gold"] += 20
                win_1 = choice
                continue
            else:
                choice_2["damage"] = choice_2["damage"] - choice["damage"]
                choice["gold"] += 20
                win_1 = choice_2
                continue
        if len(sides) == 0:
            if choice["damage"] > choice_2["damage"]: 
                choice["damage"] = choice["damage"] - choice_2["damage"]
                choice_2["gold"] += 20
                win_2 = choice
                continue
            else:
                choice_2["damage"] = choice_2["damage"] - choice["damage"]
                choice["gold"] += 10
                win_2 = choice_2
                continue
    if len(sides) == 0:
        if win_1["damage"] > win_2["damage"]:
            win_1["points"] += 1
            win_1["gold"] += 20
            win_2["gold"] += 15
            print(f"The winner of the round is {win_1['tag']}.")
            print(f"{win_1['tag']} score is {win_1['points']}.")
            time.sleep(10)
        if win_2["damage"] > win_1["damage"]:
            win_2["points"] += 1
            win_2["gold"] += 20
            win_1["gold"] += 15
            print(f"The winner of the round is {win_2['tag']}.")
            print(f"{win_2['tag']} score is {win_2['points']}.")
            time.sleep(10)

    winner()

# Function that decides if there is a game winner or if the game continues
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
        start()

    return winning

# Function that sets give the same ammount of gold to each side and sets the damage to zero
def start():
    blue["gold"] += 50
    red["gold"] += 50
    yellow["gold"] += 50
    orange["gold"] += 50
    
    blue["damage"] = 0
    red["damage"] = 0
    yellow["damage"] = 0
    orange["damage"] = 0

    main()

# The function that starts the troop_choice function
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

