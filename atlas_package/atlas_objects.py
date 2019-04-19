class Card():
	#'''
	#class Card
	#Two attribute suit and rank eg. '10ACE'
	#'''
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    
    def __str__(self):
            return(f'{self.rank}{self.suit}')

    def __repr__(self):
    	return str(self)


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



class Player():

	def __init__(self,name):
		self.stats = Player_stats() #object composition / stats

		self.name = name
		self.hand = []

	def __str__(self):
		return f'{self.name}'

	def __repr__(self):
		return str(self.name)


# player = Player('ocelot')
# print(player.__dict__)











