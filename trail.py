
from intro import intro, management_options
from players import player_name
from month import going
from characters import characters
from river import river_cross
from general_store import shop
from hunting import animal_generator, shoot_decision, food, attack

intro()
player_name()

going()

role,bank = characters()

shop(bank)


river_cross()

animal_generator()