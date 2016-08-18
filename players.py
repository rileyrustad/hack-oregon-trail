def player_name():
    print('Five players are required to play The Oregon Trail.')
    trail_dict = {}  
    players = list(range(1, 6))
    for item in players:    
        player = input("What is the name of player #{}?: ".format(item))
        trail_dict['player{}'.format(item)] = ({'name': player, 'health': 10, 'status': 10})
    return trail_dict