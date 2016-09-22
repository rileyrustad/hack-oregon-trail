
# Create a variable that counts days based on starting month of trip?

current_date= choice 

	
def travel_trail():
	import random
    from time import sleep

	# create a list of occurances that are randomly picked when the player travels the trail. Some occurances are entered into the list multiple time to simulate more common occurances.

 	occurances = [storm, nothing , nothing , nothing, death, store, animal, animal, animal, river, nothing, nothing, nothing, lost]
	print(random.choice(occurances))

	deaths= ['tubuculosis','dysentery','a gunshot wound', 'a snake bite', 'medical malpractice','starvation', 'rabies' ]

    def nothing():
        
        current_date =+ 1 
        total_mileage = +10
        print("travelling....")
        sleep(3)
        print("You have successfully travelled 1 day west. It is now day {} of your trip. Your total distance travelled is {} miles".format(current_date,total_mileage))
        return current_date =+ 1 
        return total_mileage = +10
    def storm():
     	print("A dust storm has blocked your way West. You travel in circles in search of the setting sun but are overtaken by the harsh winds"
     	current_date =+ 3
     	total_milage =-7
     	sleep(3)
    	print(\

    	'''
    	You awake to the sound of vultures shrieking from above. 
    	Your group is battered, bruised, and confused. You have 
    	lost 3 days and 7 miles to the storm. Also, Bob died. It 
    	is now day {} of your trip. Your total distance travelled 
    	is {} miles''') .format(current_date,total_mileage))

    def lost():
    	print("{} was reading the map upside down. Your group has lost 1 day".format(random.choice(players)))
    	current_date =+ 1

    def death():
    	print("{} has died from {}".format(random.choice(players), random.choice(deaths)))



chaos_factor= randint(1,4)

