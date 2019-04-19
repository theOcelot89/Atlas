def create_deck(card):
	'''
	Creates a deck with 32 cards with the classic suits
	but with range from 7 to Ace
	'''

	#assign icons to suits
	Clubs = "\u2663"
	Spades = "\u2660"
	Diamonds = "\u2666"
	Hearts = "\u2665"

	suits = (Hearts, Diamonds, Spades, Clubs)
	ranks = ('7', '8', '9', '10', 'J', 'Q', 'K', 'Ace')
	global deck
	deck = []

	#producing standard deck
	for suit in suits:
		for rank in ranks:
			deck.append(card(suit,rank))

	return deck

def create_holland_cards(deck):
	'''
	creates stack of the two bottom cards of a given deck
	'''

	holland_cards = []
	holland_cards.append(deck.pop(0))  #draw bottom card
	holland_cards.append(deck.pop(0))  #and again..
	return holland_cards

def create_table():
	'''
	creates a list of empty positions
	according to number of players
	'''
	seat = 1
	table = [(seat+x)  for x in range(7)]
	return table

def arrange_table(table,players):
	for player in players:
		while True:
			try:
				choice = int(input(f'{player.name} choose seat: '))
				assert choice in range(1,8) and type(table[choice-1]) == int, "out of range again.."

			except AssertionError as err:
				print(f'{err}')
				continue
			except:
				print('try again..')
				continue
			else:
				table[choice-1] = player
				break




def print_table(table):	#prints table empty or after arrangment

	print('          |',table[0],'|     |',table[4],'|      |',table[6],'|')
	print()
	print('|',table[3],'|                                    |',table[1],'|')
	print()
	print('            |',table[2],'|               |',table[5],'|')



def game_has_holland(deck,players):  #defines if game has 'holland player' based on number of players
	if len(players) in [3,5,7]:
		holland_cards = create_holland_cards(deck)
	else:
		holland_cards = []
	return holland_cards
	
def players(player):
	players = input('enter name of players: ').split()
	real_players = []
	for niggro in players:
		real_players.append(player(niggro))
	return real_players





#create_table('loiakjdash')





