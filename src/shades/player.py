class Player():

	def __init__(self,name):
		self.stats = Player_stats() #object composition / stats

		self.name = name
		self.hand = []

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return str(self.name)

	def give_card(self,deck,other_player): # give card to other player
		other_player.hand.append(deck.pop())

	def split(self,split_type,holland_exists,deck,chairs): #splits deck to players


		if holland_exists: # if holland player exists draw 2 bottom deck cards
			holland_cards = []
			holland_cards.append(deck.pop(0))
			holland_cards.append(deck.pop(0))


		split = list(chairs.keys())[list(chairs.values()).index(self)] + 1 #defining the chair to split first 
		if split ==6: #looping over chairs if needed
			split = 1
		
		
		while len(deck) >= split_type:

			player = chairs[split]

			for counter in range(split_type): #	give number of cards according to split type that splitter chose			
				self.give_card(deck,player)
			
			if split == len(chairs): #looping over chairs
				split = 1
				continue
			else:
				split +=1
				continue
				









# player = Player('ocelot')
# print(player.__dict__)

class Player_stats():

	def __init__(self):

		self.games = 0
		self.wins = 0
		self.loses = 0
		self.king = 0
		self.atlas = 0
		self.revolutions = 0
		self.types_of_revos = {} # will be a dictionary with 
								 #all possible card revos as keys
								 # and times they occured as values


	def __str__(self):
		return str(self)












