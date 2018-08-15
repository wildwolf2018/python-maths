'''
Finding the percentile
'''

#Finds the value that corresponds to a given percentile
def calculate_value(data, percentile):
	data.sort()
	size = len(data)
	number = -1
	index = (size * percentile * 0.01) + 0.5
	
	if index.is_integer():
		number =  data[int(index)-1]
	else:
		integral_part = int(index)
		fractional_part = index - integral_part
		number = (1 - fractional_part) * data[integral_part-1] + fractional_part * data[integral_part]
	return number

#Format a number based on whether it's an integer or not	
def format_value(number):
	if number.is_integer():
		return int(number)
	else:
		return number
	
if __name__ == '__main__':
	percentile = float(input('Enter the percentile: '))
	file = open('data.txt')
	file.seek(0, 2)
	position = file.tell()
	file.seek(0, 0)
	buffer = file.read(position)
	data_list = buffer.split()
	numerical_data = []
	
	for i in data_list:
		numerical_data.append(float(i))
			
	result = calculate_value(numerical_data, percentile)
	result = format_value(result)
	percentile = format_value(percentile)
	print('{0}th percentile is {1}'.format(percentile, result))