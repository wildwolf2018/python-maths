'''
Calculates the mean, median, variance and standard deviation
Plots the graph of population differences 
'''

import csv
import matplotlib.pyplot as plt

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

#Drwas the sctter plot
def draw_graph(x, y):
	plt.scatter(x, y, color='red')
	plt.title('Population differences from end of 1951 to end of 2017')
	plt.xlabel('years')
	plt.ylabel('difference between successive years')
	plt.axis(xmin=0.0)
	plt.grid()
	plt.show()
	
#Shows the statistcs
def calculate_stats(data):
	number_of_elements = len(data)
	diff_mean = find_mean(data, number_of_elements)
	diff_median = find_median(data, number_of_elements)
	diff_variance = find_variance(data, number_of_elements)
	diff_std = std_deviation(data, number_of_elements)
	print('Mean is {0}\nMedian is {1}\nVariance is {2}\nStandard deviation is {3}'.format(diff_mean, diff_median, diff_variance, diff_std))
	
	
if __name__ == '__main__':
	differences = []
	x_values = []
	previous_value = 0
	current_value = 0
	diff = 0
	row_number = 1
	
	with open('WWDI-USA_SP_POP_TOTL.csv') as cvs_file:          
		reader = csv.reader(cvs_file) 
		next(reader) 
		second_row  = next(reader) 
		previous_value = float(second_row[1])
		for row in reader:                         
			current_value = float(row[1])
			diff = abs(current_value - previous_value)
			differences.append(diff)
			x_values.append(row_number)
			row_number += 1
			previous_value = current_value
			
	# Plot
	differences.reverse()
	draw_graph(x_values, differences)
	calculate_stats(differences)
	
