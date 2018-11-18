'''
Creates an animated figure showing the  plotting of
20 000 points using the Henon function
'''
import matplotlib.pyplot as plt
from matplotlib import animation

#Applies tranfromations to a point
def transformation(point):
	x = point[0]
	y = point[1]
	x1 = y + 1 - (1.4 * x**2)
	y1 = 0.3 * x
	return x1, y1

#Set the radius of each point
def update_radius(i, circles):
	circles[i].radius = 0.01
	return circles,

if __name__ == '__main__':
	#Initial point
	x1, y1 = 1, 1
	x_coords = [1] #List of the x coordinates
	y_coords = [1] #List of the y coordinates
	num_iterations = 20000

	for i in range(num_iterations):
		x1, y1 = transformation((x1, y1))
		x_coords.append(x1)
		y_coords.append(y1)
	#Reference to the current figure
	fig = plt.gcf()
	#Reference to current figure's axis
	ax = plt.gca()
	#List of points to be drawn
	circles = []
	
	for i in range(num_iterations):
		circle = plt.Circle((x_coords[i], y_coords[i]), radius = 0.0)
		circles.append(circle)
		ax.add_patch(circle) 

	anim = animation.FuncAnimation(fig, update_radius, fargs = (circles,), frames=num_iterations, interval=0.0001)
	plt.axis('scaled') 
	plt.title('Henon function with {0} points'.format(num_iterations))    
	plt.show()
