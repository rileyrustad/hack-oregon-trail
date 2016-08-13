import time
import pickle

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


if __name__ == '__main__':
    choice = intro()
