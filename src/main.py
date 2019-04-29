from shades import *
from gears import *




#varieables for running the game
players = ['leo','seo','teo','sakeo','celeo']
is_first_game = True

objective_players = playerstoobjects.turn_players_to_objects(players)
holland_exists = holland.if_holland_exists(players)
print(holland_exists)









table = table.Table(objective_players)





table.arrange_table()


table.deck.shuffle()

print(table.deck)
print(table.chairs)

splitter = who_splits.who_splits(is_first_game,table.deck.deck,table.chairs)



table.deck.shuffle()

print(table.deck)

split_type = int(input(f'{splitter} enter split type:'))

splitter.split(split_type,holland_exists,table.deck.deck,table.chairs)

for player in table.players:
	print(player.name,player.hand)






#TESTS
#print(dir())
#deck = deck.Deck()
#print(deck)
#holland_cards = deck.create_holland_cards()
#print(holland_cards,deck)











