def who_splits(is_first_game,deck,chairs): #decide who splits depending...
	splitter = None
	if is_first_game: # if it is the first game 
		
		x = 1 
		for card in range(31,0,-1): 
			candidate = chairs[x]

			print(deck[card],'-',chairs[x]) #show card to each player

			if deck[card].rank == 'Ace': #if card is ace player splits
				splitter = candidate
				break
			else:
				if x == len(chairs): #looping over chairs
					x = 1
				else:
					x += 1

	else:
		splitter = atlas # if it is not atlas splits

	return splitter
