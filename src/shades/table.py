import sys
sys.path.append("/home/theocelot/Matrix/repos/Atlas/src/shades")
from cards import Card,Deck


class Table():


	def __init__(self,players):


			self.deck = Deck()
			self.players = players
			self.chairs = [ 'chair'+str(chair+1) for chair in range(len(self.players))]
			self.face = []			
			self.holland_cards = []


	def __str__(self):
		return (f'deck:{self.deck},\nplayers:{self.players},\nchairs:{self.chairs}')

			

	def arrange_table(self): # arrange by input desired chair for each player
		for player in self.players:
			while True:
				try:
					print(self.chairs)
					choice = int(input(f'{player} choose seat: '))
					
					assert choice in range(1,len(self.players)+1) and self.chairs[choice-1] == "chair"+str(choice), "out of range again.."

				except AssertionError as err:
					print(f'{err}')
					continue
				except:
					print('try again..')
					continue
				else:
					self.chairs[choice-1] = player
					break


	# def who_plays_first(self):	

	# 	for player in self.players:







			


