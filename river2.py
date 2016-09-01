
dic_people = {'player1': 'paul', 'player2': 'john', 'player3': 'rose', 'player4': 'marie', 'player5': 'robert'}
dic_supply = {1: 'boat', 2: 'plane', 3: 'canoe', 4: 'swim', 5: 'bridge'}

def probability():

    import random
    depth = (random.randint(2, 11))
    width = (random.randint(100, 301))
    chance = ((width * depth / 3311 )* 100)

    print('The river is', depth,
         'feet deep at its deepest point, and',
         width, 'feet accross.  You have a', chance,
         '% chance of crossing successfully.')

def results():
    success = 0
    result = ""

    import random
    success = (random.randint(1, 100))
    if (50< success <=100):
        print("This experience was successful with a success result of", success, " over 100.")
        return True
    else:
        print("This experience was unsuccessful with a success result of", success, " over 100.")
        return False

def cross_method():
    crossing_method = ""
    i = 0
    chain_supply = ""

    for i in dic_supply.keys():
        chain_supply = chain_supply + str(i) + ", "
    chain_supply = chain_supply[:-2]

    crossing_method = str(input("Enter the crossing method number from "+ chain_supply+ ". "))
    while(crossing_method not in chain_supply):
        print("Please select a method from the given dictionary")
        crossing_method = str(input("Enter the crossing method number from "+ chain_supply + ". "))
    return crossing_method

def intro_player():
    i_player = ""
    i = ""
    chain_player = ""
    for i in dic_people.keys():
        chain_player = chain_player + i + ", "
    chain_player = chain_player[:-2]

    i_player = str(input("Which player from the "+ chain_player + " are you? (e.g: player1) "))
    while(i_player not in chain_player):
        print("Please select a player from the given dictionary")
        i_player = str(input("Which player from the "+ chain_player + " are you? (e.g: player1) "))
    return i_player

def deplete_dic(value1, value2):
    print(value1)
    print(value2)
    print(dic_people[str(value1)])
    del dic_people[str(value1)]
    print(dic_supply[int(value2)])
    del dic_supply[int(value2)]
    print("the new dictionaries are:")
    print(dic_people)
    print(dic_supply)

def main():
    in_player = ""
    cr_method = ""

    in_player = intro_player()
    cr_method = cross_method()
    probability()
    final_result = results()
    if not final_result:
        deplete_dic(in_player, cr_method)

main()








