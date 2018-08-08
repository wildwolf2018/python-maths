''' 
Draws the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

color_index = 1;

def divideRange(start, final, increment):
    time_values = []
    while start < final:
        time_values.append(start)
        start = start + increment
    return time_values

def chooseColor():
	if color_index == 1:
		return 'r'
	elif color_index == 2:
		return 'g'
	elif color_index == 3:
		return 'b'
	else:
		return 'k'
	
def drawGraph(xcoord_list, ycoord_list):
	graph_color = chooseColor()
	plt.plot(xcoord_list, ycoord_list, linewidth=2, color=graph_color)
	
def findDistances(time_values, init_velocity, angle):
	gravity = 9.8
	_cos = init_velocity * math.cos(angle)
	_sin = init_velocity * math.sin(angle)
	
	#Holds horizontal distances
	sx = []
	#Holds vertical distances
	sy = []
	for t in time_values:
		xcoord = _cos * t
		sx.append(xcoord)
		ycoord = _sin * t - (0.5 * gravity * (t**2))
		sy.append(ycoord)

	drawGraph(sx, sy)
	
if __name__ == '__main__':
	number_of_trajectories = int(input('Enter the number of trajectories: '))
	gravity = 9.8
	legend = []
	
	for i in range(1, number_of_trajectories+1):
		color_index = i
		legend.append('path ' + str(i))
		init_velocity = float(input('Enter the initial velocity of trajectory: '))
		theta = float(input('Enter the angle of trajectory: '))
		angle = math.radians(theta)
		time_of_flight = 2*init_velocity*math.sin(angle)/gravity
		print('Flight time for trajectory{0}: {1:.3} seconds'.format(i, time_of_flight))
		result = divideRange(0, time_of_flight, 0.001)
		findDistances(result, init_velocity, angle)
		
	plt.xlabel('horizontal distance')
	plt.ylabel('vertical distance')
	plt.axis('tight')
	plt.axis(ymin=0.0)
	plt.legend(legend)
	plt.show()