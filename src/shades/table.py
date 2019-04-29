import sys
sys.path.append("/home/theocelot/Matrix/repos/Atlas/src/shades")
from deck import Card,Deck


class Table():


	def __init__(self,players):


			self.deck = Deck()
			self.players = players
			self.face = []			
			self.chairs = {chair+1:'' for chair in range(len(self.players))}

	def __str__(self):
		return (f'{self.deck},\n{self.players},\n{self.chairs}')

			

	def arrange_table(self): # arrange by input desired chair for each player
		for player in self.players:
			while True:
				try:
					choice = int(input(f'{player} choose seat: '))
					assert choice in range(len(self.players)+1) and self.chairs[choice] == "", "out of range again.."

				except AssertionError as err:
					print(f'{err}')
					continue
				except:
					print('try again..')
					continue
				else:
					self.chairs[choice] = player
					break


	# def who_plays_first(self):	

	# 	for player in self.players:







			


