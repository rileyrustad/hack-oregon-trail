# REM Function for determining if river crossing is a success.

supplies={'oxen':4,'food':1000,'clothing':30,'ammunition':40,'wagon wheel':3,
	'wagon axle':2,'wagon tongue':2}

people={'per1':'emily','per2':'zeke','per3':'hope','per4':'ezra',
	'per5':'lourdes'}

def river_cross():

	''' This function determines whether crossing a river is a success or not.'''

	import random

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





