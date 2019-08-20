from card_ranks import *






def same_rank(play):

	for i in range(len(play)-1):
			if board[i].rank == board[i+1].rank:
				same_rank = True
				continue
			else:
				same_rank = False
				break
	return same_rank






def valid(play,board):


	if len(play) > 1:
		same_rank(play)




	

	
	
