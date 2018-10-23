'''
Simulation in which a deck of 52 cards  is shuffled and then
displayed on the screen
'''
from random import shuffle

class Card:
	def __init__(self, suit, rank):                      
		self.suit = suit                                 
		self.rank = rank 

def main():
	card_rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ace', 'king', 'queen', 'jack']
	suites = ['spades', 'clubs', 'diamonds', 'hearts']
	card_list = []

	for i in suites:
		for j in card_rank:
			card = Card(i, j)
			card_list.append(card)

	shuffle(card_list)

	for _card in card_list:
		print('{0} of {1}'.format(_card.rank, _card.suit))

if __name__ == '__main__':
	main()