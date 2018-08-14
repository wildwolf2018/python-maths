'''
Calculates the mean, median, variance and standard deviation
Plots the graph of population differences 
'''

#Calculates the mean
def find_mean(data, data_size):
	total = sum(data)
	mean = total / data_size
	return mean

#Calculates the median 
def find_median(data, data_size):
	data.sort()
	median = -1
	#Determines whether number of data items is even or odd and
	#then calculates medain based on the result of test
	if data_size % 2 == 0:
		#Position of first number in sorted list bigger than the median
		first_num_pos = int(number_of_elements / 2)
		#Position of first number in sorted list smaller than the median
		second_num_pos = first_num_pos - 1
		median = (data[first_num_pos] + data[second_num_pos]) / 2
	else:
		median_position = (data_size // 2)
		median = data[median_position]
	return median
		
#Calculates the variance
def find_variance(data, data_size):
	mean = find_mean(data, data_size)
	total = 0
	
	for value in data:
		square_diff = (value - mean) ** 2
		total += square_diff
	return total / data_size

#Calculates the standard deviation
def std_deviation(data, data_size):
	variance = find_variance(data, data_size)
	return variance ** 0.5

if __name__ == '__main__':
	population =  [100, 60, 70, 900, 100, 200, 500, 500, 503, 600, 1000, 1200] 
	print(population)
	number_of_elements = len(population)
	population_var = find_variance(population, number_of_elements)
	population_std = std_deviation(population, number_of_elements)
	print('Variance is {0}'.format(population_var))
	print('Standard deviation is {0}'.format(population_std))
