from shades.cards import *
from shades.player import *
from shades.table import *
from gears.playerstoobjects import *
from gears.setup_checks import *




#varieables for running the game
players = ['leo','seo','teo','sakeo','celeo']


#turn named players to objective players
objective_players = turn_players_to_objects(players)

#turn true in start of game session
is_first_game = True

#return true if player number is odd
holland_exists = if_holland_exists(players)
print('holland exists??',holland_exists,'\n')







###SETUP GAME - THIS HAPPENS ONCE PER GAME SESSION

#creating game_game_table (chairs and deck), according to number of players 
game_table = Table(objective_players)
print(game_table,len(game_table.deck),'\n')


#arrange which player sits in which chair
game_table.arrange_table()




###MAIN FLOW - THIS HAPPENS ONCE PER GAME


#shuffling the deck
game_table.deck.shuffle()
print(game_table,len(game_table.deck),'\n')

#find the splitter
splitter = who_splits(is_first_game,game_table.deck.deck,game_table.chairs)

#ask the splitter for split type
split_type = int(input(f'{splitter} enter split type:'))

#shuffle deck again
game_table.deck.shuffle()
print(game_table,len(game_table.deck),'\n')



#split the deck
splitter.split(split_type,holland_exists,game_table.deck.deck,game_table.chairs,game_table.holland_cards)

print(game_table,len(game_table.deck),'\n')

#print players hands
for player in game_table.players:
	print(player,player.hand)


print()

#check who plays first
active_player = who_plays_first(is_first_game,game_table.chairs)
print(game_table.holland_cards)

active_player.play(game_table.face)





