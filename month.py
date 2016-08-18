def going():
    
    choice = 0
    while choice not in [1,2,3,4,5,6, '1','2','3','4','5','6']:
    
        choice = input('''When ya going? Pick a month:     
            1.  March
            2.  April
            3.  May
            4.  June
            5.  July
            6.  Ask for advice
    
        ''')     
        
    if choice == '1': return 'March'
    elif choice == '2': return 'April'
    elif choice == '3': return 'May'
    elif choice == '4': return 'June'
    elif choice == '5': return 'July'
    elif choice == '6': 
        print( '''If you leave too early there will not be any grass for your oxen to eat. \n
            If you leave to late you may not get to Oregon before winter comes. \n
            If you leave at just the right time, there will be green grass and the weather will still be cool.''' )
        going()