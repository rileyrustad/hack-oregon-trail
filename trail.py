from intro import intro, management_options
from players import player_name
from month import going
from characters import characters
from general_store import shop
from hunting import animal_generator, shoot_decision, food, attack

intro()
player_name()

going()

role,bank = characters()

shop()

animal_generator() #Hunting Function
