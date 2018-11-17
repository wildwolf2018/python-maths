
'''
 Draws the Sierpin´ski Triangle using a specified number of points
 The starting point from which new points will be generated is (0,0) 
'''

from matplotlib import pyplot as plt
import random

#Transforms a point with coordinates x,y
def transformation_1(x, y):    
	 x1 = 0.5 * x   
	 y1 = 0.5 * y  
	 return x1, y1

#Transforms a point with coordinates x,y
def transformation_2(x, y):  
	x1 = 0.5 * x + 0.5    
	y1 = 0.5 * y + 0.5    
	return x1, y1

#Transforms a point with coordinates x,y
def transformation_3(x, y):  
	 x1 = 0.5 * x + 1  
	 y1 = 0.5 * y    
	 return x1, y1

#Determines which tranformation must be applied bases on calculated probability
def calc_probability(distr):
	prob = random.random()
	for index, value in enumerate(distr):
		if prob <= value:
			return index
	return len(distr) - 1 

#Calculates the probability distribution for the given events
def calc_distribution(probabilty):
	distribution = []
	sum = 0
	for value in probabilty:
		sum += value
		distribution.append(sum)
	return distribution

#Applies tranfromations to the points and stores the results in lists
def transform_points(distr):
	p1, p2 = 0, 0
	x = [0]
	y = [0]
	transformations = [transformation_1, transformation_2, transformation_3]

	for i in range(num_points):
		index = calc_probability(distr)
		func = transformations[index]
		p1, p2 = func(p1, p2)
		x.append(p1)
		y.append(p2)
	return x, y

if __name__ == '__main__':
	num_points = int(input('Enter the number of points: '))
	#Probabilities of the given tranformations
	probabilty = [1/3, 1/3, 1/3]
	distr = calc_distribution(probabilty)
	x_coords, y_coords = transform_points(distr)

	# Plot the points    
	plt.plot(x_coords, y_coords, '.', color='red')
	plt.xlabel('X')
	plt.ylabel('Y')    
	plt.title('Sierpinski triangle with {0} points'.format(num_points))    
	plt.show()







