


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


	def split(self,split_type,holland_exists,deck,chairs,holland_cards): #splits deck to players
		
		if holland_exists: # if holland player exists draw 2 bottom deck cards

			holland_cards.append(deck.pop(0))
			holland_cards.append(deck.pop(0))
		
		split_index = chairs.index(self) + 1 #defining the chair to split first // 
		if split_index ==5: #looping over chairs if needed
			split_index = 1
		
		
		while len(deck) >= split_type:

			player = chairs[split_index]

			for counter in range(split_type): #	give number of cards according to split type that splitter chose			
				self.give_card(deck,player)
			
			if split_index == len(chairs)-1: #looping over chairs
				split_index = 0
				continue
			else:
				split_index +=1
				continue

		return holland_cards

	def play(self, board):

		print(self.hand)

		while True:
			try:
				choice = input('choose card/s or go paso: ')
				print(choice) 
				assert choice.lower() =='paso' or all(isinstance(x, int) for x in choice), 'wrong choice'
				

			except AssertionError as err:
				print(err)	
			else:
				#choice = list(map(int,(input('choose card or cards: ').split())))  # choose index or indexes of cards
				play = [self.hand[index] for index in choice] # defining actuall cards to play			
				if valid_play()	and valid_move():
					board.append(play)
					break





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

















