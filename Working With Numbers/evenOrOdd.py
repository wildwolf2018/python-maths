#Author: Thabo Thage
#Date: 01 August 2018

#Displays the number followed by the next 9 even or odd numbers
def printResults(number):
	offSet = 0
	for x in range(0, 10):
		if x <= 8:
			print('%d, '%(number + offSet), end='')
			offSet += 2 
		else:
			print('%d. '%(number + offSet))

#Determines if a number is even or odd			
def isEven(number):
	if number % 2 == 0:
		print('\n%d is even'%(number))
		printResults(number)
	else:
		print('\n%d is odd'%(number))
		printResults(number)

if __name__ == "__main__":
	userInput = float(input('Enter a number: '))
	if userInput > 0 and userInput.is_integer():
		isEven(userInput)
	else:
		print('Number must be a positive integer')
	