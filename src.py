from atlas_package import atlas_functions, atlas_objects
import random

'welcome Atlas'

#create table(empty list positions) 
table = atlas_functions.create_table()

#print table
atlas_functions.print_table(table)

#input players
players = atlas_functions.players(atlas_objects.Player)

#arrange table
atlas_functions.arrange_table(table,players)

#print arranged table
atlas_functions.print_table(table)

#create deck
deck = atlas_functions.create_deck(atlas_objects.Card)

#shuffle deck
random.shuffle(deck)

#check for holland player and create holland cards if true
holland_cards = atlas_functions.game_has_holland(deck, players)







# TESTS
print(players)
print(deck, len(deck))
print(holland_cards, len(holland_cards))




