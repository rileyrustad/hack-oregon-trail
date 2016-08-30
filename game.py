import time
import pickle
import random
from random import randint

def intro():
    '''
    gives player options to start, learn about the game, or change settings.
    :return:
    '''
    valid_choices = ['1','2','3','4','5','6']
    options = \
'''You may:

1. Travel the trail
2. Learn about the trail
3. See the Oregon Top Ten
4. Turn sound off
5. Choose Management Options
6. End

What is your Choice?: '''

    story = \
'''
Try taking a journey by covered
wagon across 2000 miles of plains,
rivers, and mountains. Try! On the
plains, will you slosh your oxen
through ud and watter-filled ruts
or will you plod through dust six
inches deep?

How will you cross the rivers? If
you have money, you might take a
ferry (if there is a ferry). Or,
you can ford the river and hope
you and your wagon aren't swalled
alive!

What about supplies? Well, if you're
low on food you can hunt. You might
get a buffalo ... you might. And
there are bear in the Mountains.

At the Dalles, you can try navigating
the Columbia River, but if running
the rapids with a makeshift raft
makes you queasy, better take the
Barlow Road.

If for some reason you don't
survive -- your wagon burns, or
thieves steal your oxen, or you
run out of provisions, or you die
of cholera -- don't give up! Try
again... and again... until your
name is up owith the others on
The Oregon Top Ten.

The software team responsible for
Creation of this product is the
Hack University Python Foundations
class.
'''
    print('Welcome to the Oregon Trail!')
    choice = input(options)
    while choice not in valid_choices:
        print('"{}" is not a valid response, try again'.format(choice))
        time.sleep(2)
        choice = input(options)
    if choice == '1':
        print('This functionality has not been made yet')
        time.sleep(3)
        intro()
    elif choice == '2':
        print(story)
        time.sleep(10)
        intro()
    elif choice == '3':
        top_ten = pickle.load(open('topten.txt','rb'))
        for position, name in top_ten:
            print(position, name)
        time.sleep(3)
        intro()
    elif choice == '4':
        print('This functionality has not been made yet')
        time.sleep(3)
        intro()
    elif choice == '5':
        management_options()
    elif choice == '6':
        exit()


def management_options():
    valid_inputs = ['1','2','3','4']
    options = \
'''
You may:

1. See the current Top Ten List
2. Erase the current Tob Ten List
3. Erase saved games
4. Return to the main menu

What is your choice?: '''
    choice = input(options)
    while choice not in valid_inputs:
        print('"{}" is not a valid response, try again'.format(choice))
        time.sleep(2)
        choice = input(options)

    if choice == '1':
        top_ten = pickle.load(open('topten.txt','rb'))
        for position, name in top_ten:
            print(position, name)
        time.sleep(3)
        management_options()

    elif choice == '2':
        top_ten = [('Top Ten:','')]
        for i in range(1,11):
            top_ten.append((i,''))
        pickle.dump(top_ten,open('topten.txt','wb'))
        for position, name in top_ten:
            print(position, name)
        time.sleep(3)
        management_options()

    elif choice == '3':
        print('Feature has not been built yet')
        time.sleep(2)
        management_options()

    elif choice == '4':
        intro()

def player_name():
    print('Five players are required to play The Oregon Trail.')
    trail_dict = {}
    players = list(range(1, 6))
    for item in players:
        player = input("What is the name of player #{}?: ".format(item))
        trail_dict['player{}'.format(item)] = ({'name': player, 'health': 10, 'status': 10})
    return trail_dict


def going():
    choice = 0
    while choice not in [1, 2, 3, 4, 5, 6, '1', '2', '3', '4', '5', '6']:
        choice = input('''When ya going? Pick a month:     
            1.  March
            2.  April
            3.  May
            4.  June
            5.  July
            6.  Ask for advice

        ''')

    if choice == '1':
        return 'March'
    elif choice == '2':
        return 'April'
    elif choice == '3':
        return 'May'
    elif choice == '4':
        return 'June'
    elif choice == '5':
        return 'July'
    elif choice == '6':
        print('''If you leave too early there will not be any grass for your oxen to eat. \n
            If you leave to late you may not get to Oregon before winter comes. \n
            If you leave at just the right time, there will be green grass and the weather will still be cool.''')
        going()

def characters():
    choice = input('''Many kinds of people made the trip to Oregon.
You may:
1.	Be a banker from Boston
2.	Be a carpenter from Ohio
3.	Be a farmer from Illinois
What is your choice? ''')
    if choice == '1':
        print ('You are a banker; you have $1600.')
        return 'Banker',1600
    elif choice == '2':
        print ('You are a carpenter; you have $800.')
        return 'Carpenter',800
    elif choice == '3':
        print ('You are a farmer; you have $400.')
        return 'Farmer',400
    else:
        print ('Please choose 1, 2 or 3.')
        characters()


def shop():
    store = {
        'oxen': (40, 'yoke'),
        'food': (.20, 'lb'),
        'clothing': (10, 'set'),
        'ammunition': (20, '20 round box'),
        'spare parts': (10, 'part')
    }

    supplies = {
        'oxen': [0, 'yokes'],
        'food': [0, 'lbs'],
        'clothing': [0, 'sets'],
        'ammunition': [0, 'boxes'],
        'spare parts': [0, 'parts']
    }

    start_money = 1600
    end_money = start_money

    print('Welcome to the GENERAL STORE!\n\nInventory:\n----------')
    for i in store:  # prints the store's inventory
        print('+ {}'.format(i.capitalize()))
    print("Press 'e' to exit the store\n")
    while end_money >= 0:
        print('You have ${} to spend.'.format(end_money))
        buy = input('What supplies would you like to buy? ').lower()
        if buy in store:
            purchase = int(input(
                '\n{} costs {} dollars per {}.\nYou currently have {}.\nEnter the amount you wish to buy: '.format(buy,
                                                                                                                   store[
                                                                                                                       buy][
                                                                                                                       0],
                                                                                                                   store[
                                                                                                                       buy][
                                                                                                                       1],
                                                                                                                   supplies[
                                                                                                                       buy][
                                                                                                                       0])))
            if (purchase * store[buy][0]) <= end_money:
                print('\nSuccess!')
                supplies[buy][0] = purchase  # adds purchase to user's supplies dict
                total = 0
                for each in supplies:  # for loop recalculates how much money is left
                    total += supplies[each][0] * store[each][0]
                end_money = start_money - total
            else:
                print("\nSorry, you don't have enough money.\n")
        elif buy.lower() == 'e':
            print('\nThanks for shopping at the GENERAL STORE!\nRemaining cash: ${}\nSupplies:'.format(
                end_money))  # prints how much money is left
            for i in supplies:  # iterates over and prints each item in the user's inventory
                print('{} - {} {}'.format(i.capitalize(), supplies[i][0], supplies[i][1]))
            return


def river_cross():

	''' This function determines whether crossing a river is a success or not.'''



	depth=(random.randint(2,10))
	width=(random.randint(100,300))
	chance=(width*depth/3000*100)
	success=(random.randint(1,100))
	print('The river is',depth,
      'feet deep at its deepest point, and',
      width,'feet accross.  You have a', chance,
      '% chance of crossing successfully.')
	choice = input('''You must choose how to cross:

1.  Attempt to ford the river.
2.  Caulk the wagon and float it accross.
3.  Wait to see if conditions improve.

What is your choice?\n''')
	if choice == '1':
		print('\nYou attempt to ford the river...\n')
		if (success) <= (chance):
			print('\nYou have successfully navigated the river without incident!\n')
			return True
		else:
			print('\nYour river crossing was not a success.\n')
			return False
	elif choice == '2':
		# day = day +1
		print('\nYou spend a day caulking the wagon and attempt to float accross...\n')
		(success)=((success)*2)
		if (success) <= (chance):
			print('\nYou are able to float accross the river safely.\n')
			return True
		else:
			print('\nYour river crossing was not a success\n')
			return False
	elif choice == '3':
		# day = day +1
		print('\nYou wait a day to see if conditions improve.\n')
		return river_cross(supplies,people)
	else:
		return '\nPlease choose 1, 2, or 3.\n'

def animal_generator():
    check_out = input("Something is rustling in the bushes. Would you like to go check it out? (y/n) ")
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
    decision = input(("A {} jumps out! Would you like to shoot the {}? (y/n) ").format(animal, animal))
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
    statement = ("You have killed the {}.").format(animal)
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
    statement = ("You have been attacked by the {}!").format(animal)
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

if __name__ == "__main___":
    intro()
    player_name()

    going()

    role, bank = characters()

    shop()

    river_cross()

    animal_generator()