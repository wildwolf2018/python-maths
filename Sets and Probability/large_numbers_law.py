'''
The expectation of rolling a six sided die is calculated and
the average results from a number of trials is calculated
The results veriy that the 'law of large numbers' is true
'''
from random import randrange

def find_expectation(probablities):
	_expectation = 0
	keys = probablities.keys()

	for key in keys:
		_expectation += key * probablities[key]

	return _expectation

def find_trials_average(sample_space, num_trials):
	events = [] #List to hold the event that occured in each trial
	min_value = min(sample_space)
	max_value = max(sample_space)
	rand_number = 0 # Event that occured

	for index in range(num_trials):
		rand_number = randrange(min_value, max_value+1)
		events.append(rand_number)

	average = sum(events) / num_trials
	return average

def main():
	'''List of all possible evevts together with their 
	   associated probabilities'''
	probablities = { 1: 1/6, 2: 1/6, 3: 1/6, 4: 1/6, 5: 1/6, 6: 1/6}
	num_of_trials = [100, 1000, 10000, 100000, 500000]
	expect = find_expectation(probablities)
	print('Expected value = {0:.2f}'.format(expect))

	for trials in num_of_trials:
		trials_average = find_trials_average(probablities.keys(), trials)
		print('Trials: {0} Trial average {1}'.format(trials, trials_average))

if __name__ == '__main__':
	main()