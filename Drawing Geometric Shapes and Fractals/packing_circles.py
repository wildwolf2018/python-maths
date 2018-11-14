'''
Determines and draws the number of circles with radius 0.5 
can fit inside a square with a specified length.
'''

from matplotlib import pyplot as plt

#Creates a square patch and adds it to the axis
def create_square(length):      
	square = plt.Polygon([(1, 1), (length, 1), (length, length), (1, length)], closed = True, fc='gray')    
	ax.add_patch(square)    

#Creates a circle patch and adds it to the axis
def create_circle(axis, x, y, radius):
	 circle = plt.Circle((x, y), radius, fc='red', ec='blue') 
	 return circle

if __name__ == '__main__': 
	s_length = float(input('Enter the length of a side of the square: '))
	if s_length > 1.0:
		#The actual length of the square drawing area on which the circles will be drawn
		canvas_width = int(s_length - 1.0)
		num_circles = canvas_width ** 2 #The number of circles that can be drawn inside the square
		start_x = 1.5
		centre_x = start_x #x coordinate of the centre of the first circle
		centre_y = start_x #y coordinate of the centre of the first circle
		ax = plt.axes(xlim = (1, s_length), ylim = (1, s_length))
		ax.set_aspect('equal')
		radius = 0.5 #The radius of each circle
		create_square(s_length) 

		for i in range(1, num_circles + 1):
			circle = create_circle(ax, centre_x, centre_y, radius)
			ax.add_patch(circle)
			centre_x += 1.0
			if i % canvas_width == 0:
				centre_y += 1.0
				centre_x = start_x
		plt.show()
		print('The number of circles with radius={0},'.format(radius))
		print('that can fitted inside a square with side length={0} is {1}'.format(s_length, num_circles))
	else:
		print('The length of the square must be greater than 1')
