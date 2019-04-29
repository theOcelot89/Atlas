import random


class Card():
	"""Card Class. Has two attributes, rank(9,10,K,ACE) and suit(diamonds etc)"""

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return(f'{self.rank}{self.suit}')

	def __repr__(self):
		return str(self)




class Deck():
	'''Deck Class.
Attributes'''

	def __init__(self):
		self.deck = []

		Clubs = "\u2663"
		Spades = "\u2660"
		Diamonds = "\u2666"
		Hearts = "\u2665"

		suits = (Hearts, Diamonds, Spades, Clubs)
		ranks = ('7', '8', '9', '10', 'J', 'Q', 'K', 'Ace')

		#producing standard deck
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		return(f'{self.deck}')

	def __repr__(self):
		return str(self)

	def __len__(self):
		return len(self.deck)

	def shuffle(self): #shuffles the deck
		random.shuffle(self.deck)




#TESTS
#deck = Deck()
# deck.shuffle()
#print(deck, len(deck))
#print(deck.deck[0])
# print(str(deck))
# print(type(deck))
# print(deck.__doc__)
