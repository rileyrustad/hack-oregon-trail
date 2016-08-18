
"""
players = {}

for i in range(5):
	if i == 0:
		players[0] = input("What is your name? ")
	else:
		players['player {}'.format(i)] = input("What is player {}'s name? ".format(i+1))

money = 1600

inventory = {
	'oxen': 6,
	'bullets': 1000,
	'clothes': 15,
	'food': 1000,
	'spare parts':{
		'wagon wheel': 2,
		'axles': 2, 
		'wagon tongue': 2
		}
	}

cost = {
	'oxen': 40,
	'bullets': 2,
	'clothes': 10,
	'food': .2,
	'spare parts':{
		'wagon wheel':10,
		'axles': 10, 
		'wagon tongue': 10
		}
	}

store = ['oxen', 'food', 'clothing', 'ammunition', 'spare parts']

shop = {
		'1': ('oxen', 40, 'yoke'),
		'2': ('food', .20, 'lb.'),
		'3': ('sets of clothes', 10, 'set'),
		'4': ('ammunition', 2, 'box'),
		'5': ('spare parts', 10, 'part')
		}

def inv(store):
	x=0
	for i in store:
		x+=1
		print('{}. {}'.format(x,i))
	#maybe put the following in new function?
	inpt = input('What would you like to shop for? ')
	#if in range int(input) statement
	if int(inpt) in range(1,6):
		print('{} is ${} per {} '.format(shop[inpt][0], shop[inpt][1], shop[inpt][2]))
		purchase = input('Please enter the amount you wish to purchase ')

inv(store)


def shop(money, price, quantity):
	if price*quantity < money:
		print('you bought {} stuff!'.format(quantity))
	else:
		print("sorry, you don't have enough money.")
shop(1600, 40, 6)

"""

#Store function

store = {
	'oxen':(40,'yoke'),
	'food':(.20, 'lb'),
	'clothing':(10,'set'),
	'ammunition':(20, '20 round box'),
	'spare parts':(10, 'part')
	}

supplies = {
	'oxen':[0, 'yokes'],
	'food':[0, 'lbs'],
	'clothing':[0,'sets'],
	'ammunition':[0,'boxes'],
	'spare parts':[0, 'parts']
}

start_money = 1600

def shop():
	end_money = start_money
	print('Welcome to the GENERAL STORE!\n\nInventory:\n----------')
	for i in store: #prints the store's inventory
		print('+ {}'.format(i.capitalize()))
	print("Press 'e' to exit the store\n")
	while end_money >= 0:
		print('You have ${} to spend.'.format(end_money))
		buy = input('What supplies would you like to buy? ').lower()
		if buy in store:
			purchase = int(input('\n{} costs {} dollars per {}.\nYou currently have {}.\nEnter the amount you wish to buy: '.format(buy,store[buy][0],store[buy][1],supplies[buy][0])))
			if (purchase * store[buy][0]) <= end_money:
				print('\nSuccess!')
				supplies[buy][0] = purchase#adds purchase to user's supplies dict
				total = 0
				for each in supplies: #for loop recalculates how much money is left
					total += supplies[each][0]*store[each][0]
				end_money=start_money-total
			else:
				print("\nSorry, you don't have enough money.\n")
		elif buy.lower() == 'e':
				print('\nThanks for shopping at the GENERAL STORE!\nRemaining cash: ${}\nSupplies:'.format(end_money))#prints how much money is left
				for i in supplies:#iterates over and prints each item in the user's inventory
					print('{} - {} {}'.format(i.capitalize(), supplies[i][0], supplies[i][1]))
				return

shop()