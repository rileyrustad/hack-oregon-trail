# HUNTING FUNCTIONS
from random import randint
#Animal appears    
def animal_generator():
    check_out = input("Something is rustling in the bushes. Would you like to go check it out? ")
    if check_out == "y":
        animal = randint(1,4)
        if animal == 1:
            return shoot_decision("squirrel")
        elif animal == 2:
            return shoot_decision("rabbit")
        elif animal == 3:
            return shoot_decision("deer")
        else:
            return shoot_decision("bear")
    else:
        print("You've decided to continue down the road.")
#Animal is killed, attacks, or is missed
def shoot_decision(animal):
    decision = input(("A {} jumps out! Would you like to shoot the {}? ").format(animal, animal))
    if decision == "y":
        result = randint(1,3)
        if result == 1:
            food(animal)
        elif result == 2:
            print(("The {} ran away.").format(animal))
            bullets_wasted = randint(1,3)
            inventory['bullets'] -= bullets_wasted
            if bullets_wasted == 1:
                print("You've wasted 1 bullet.")
            else:
                print(("You've wasted {} bullets.").format(bullets_wasted))
        else:
            attack(animal)
    else:
        print(("You've decided to spare the {}'s life.").format(animal))
#Animal is killed
def food(animal):
    statement = ("You have killed the {}").format(animal)
    print(statement)
    if animal == "squirrel":
        print("You've received 1 pound of food!")
        inventory['food'] += 1
    elif animal == "rabbit":
        print("You've received 5 pounds of food!")
        inventory['food'] += 5
    elif animal == "deer":
        print("You've received 80 pounds of food!")
        inventory['food'] += 80
    else:
        print("You've received 800 pounds of food!")
        inventory['food'] += 800
    bullets_wasted = randint(1,3)
    inventory['bullets'] -= bullets_wasted
    if bullets_wasted == 1:
        print("You used 1 bullet.")
    else:
        print(("You used {} bullets.").format(bullets_wasted))
#Animal Attacks   
def attack(animal):
    statement = ("You have been attacked by the {}").format(animal)
    print(statement)
    if animal == "squirrel":
        print("You've lost 1 point of health!")
        player['health'] += 1
    elif animal == "rabbit":
        print("You've lost 5 points of health!")
        player['health'] += 5
    elif animal == "deer":
        print("You've lost 80 points of health!")
        player['health'] += 80
    else:
        print("You've lost 800 points of health!")
        player['health'] += 800
