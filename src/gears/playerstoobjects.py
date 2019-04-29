import sys
sys.path.append("/home/theocelot/Matrix/repos/Atlas/src/shades")
from player import Player


def turn_players_to_objects(players): #take list of name and turn them into objects
	objective_players = []
	for name in players:
		objective_players.append(Player(name))

	return objective_players


#players = turn_players_to_objects(['leo','seo'])

#print(players[0].hand)

