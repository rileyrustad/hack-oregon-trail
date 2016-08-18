
#Store function

def shop():

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