'''
Draws a graph showing 20 000 iterations of the Henon function
'''
import matplotlib.pyplot as plt

#Applies tranfromations to a point
def transformation(point):
	x = point[0]
	y = point[1]
	x1 = y + 1 - (1.4 * x**2)
	y1 = 0.3 * x
	return x1, y1

if __name__ == '__main__':
	#Initial point
	x1, y1 = 1, 1
	x_coords = [1]
	y_coords = [1]
	num_iterations = 20000

	for i in range(num_iterations):
		x1, y1 = transformation((x1, y1))
		x_coords.append(x1)
		y_coords.append(y1)
	plt.axes(xlim=(-1.5, 1.5), ylim=(-0.4, 0.4))
	plt.plot(x_coords, y_coords, '.')
	plt.xlabel('X')
	plt.ylabel('Y')    
	plt.title('Henon function with {0} points'.format(num_iterations))    
	plt.show()
