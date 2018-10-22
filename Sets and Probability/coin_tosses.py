'''
Game where the computer tosses a fair coin. The computer starts the game with a
certain amount on hand . The cpmouter wins R1.00 for heads and losses R1.50 for tails.
The game is over when the computer's balance is less or equal to 0.
'''
from random import randint

def main():
	head = 1
	tail = 0
	num_tosses = 0
	balance = float(input('Enter your starting amount: '))

	while balance >= 0:
		num_tosses += 1
		rand_number = randint(1, 2)
		if rand_number == 1:
			balance += 1.0
			print('Heads: Current amount: {0}'.format(balance))
		else:
			balance -= 1.5
			print('Tails: Current amount: {0}'.format(balance))

	print('Game over :( Current amount {0}. Coin tosses: {1}'.format(balance, num_tosses))

if __name__ == '__main__':
	main()