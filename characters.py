
#Oregon Trail Characters
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
        characters():

