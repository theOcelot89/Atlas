def who_splits(is_first_game,deck,chairs): #decide who splits depending...
	splitter = None
	if is_first_game: # if it is the first game 
		print("give cards to players till ace")
		
		x = 0
		for card in range(31,0,-1): 
			candidate = chairs[x]

			print(deck[card],'-',chairs[x]) #show card to each player

			if deck[card].rank == 'Ace': #if card is ace player splits
				splitter = candidate
				break
			else:
				if x == len(chairs)-1: #looping over chairs
					x = 0
				else:
					x += 1

	else:
		splitter = atlas # if it is not atlas splits

	return splitter


def who_plays_first(is_first_game,players): #checks who plays first in game, depending if its first game of game session

	active_player = None
	print("checking for 7diamond in players' hands")
	
	if is_first_game:
		for player in players:
			if active_player:
				break
			for card in player.hand:
				print(card)
				if card.suit == "\u2666" and card.rank == '7':
					active_player = player
					break
					
	else:
		active_player = atlas

	print(f'{active_player} plays first!')
	return active_player



def if_holland_exists(players):
	return len(players) in [3,5,7]


