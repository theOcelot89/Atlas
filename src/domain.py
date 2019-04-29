from shades import *
from gears import *




#varieables for running the game
players = ['leo','seo','teo','sakeo','celeo']


#turn named players to objective players
objective_players = playerstoobjects.turn_players_to_objects(players)

#turn true in start of game session
is_first_game = True

#return true if pplayer number is odd
holland_exists = holland.if_holland_exists(players)
print(holland_exists)







###SETUP GAME - THIS HAPPENS ONCE PER GAME SESSION

#creating game_game_table (chairs and deck), according to number of players 
game_table = table.Table(objective_players)
print(game_table)


#arrange which player sits in which chair
game_table.arrange_table()





###MAIN FLOW - THIS HAPPENS ONCE PER GAME


#shuffling the deck
game_table.deck.shuffle()
print(game_table)

#find the splitter
splitter = who_splits.who_splits(is_first_game,game_table.deck.deck,game_table.chairs)

#shuffle deck again
game_table.deck.shuffle()
print(game_table.deck)


#ask the splitter for split type
split_type = int(input(f'{splitter} enter split type:'))

#split the deck
splitter.split(split_type,holland_exists,game_table.deck.deck,game_table.chairs)

print(game_table)

for player in game_table.players:
	print(player.name,player.hand)



