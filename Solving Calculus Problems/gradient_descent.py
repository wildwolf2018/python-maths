'''
Finds the minimum value of a single-varaible function
as specified by the user
'''

import math
from sympy import Derivative, Symbol, sympify, solveset, S
import matplotlib.pyplot as plt

#Finds the minimum values using gradient ascent algorithm
def gradient_descent(start_value, func, derivative, var):
	#Check whether the first drivative exists
	if solveset(derivative, var, domain=S.Reals) == S.EmptySet:
		print('Solution for {0}=0 does not exist'.format(func))        
		return 
	epsilon =  1e-6    
	step_size = 1e-4 
	x_old = start_value
	x_new = x_old - step_size * derivative.subs({var:x_old}).evalf() 
	x_values = []
	y_values = []
	x_values.append(x_new)
	y_values.append(func.subs({var:x_new}))

	while abs(x_old - x_new) > epsilon:
		x_old = x_new
		x_new = x_old - step_size * derivative.subs({var:x_old}).evalf() 
		x_values.append(x_new)
		y_values.append(func.subs({var:x_new}))

	return x_new, x_values, y_values

#Plots the graph of the user specified function
def create_function_graph(x_values):
	last = x_values[len(x_values)-1]; first = x_values[0]
	lower_bound_x = 0; upper_bound_x = lower_bound_x
	lower_bound_y = 0; upper_bound_y = lower_bound_y
	y_array = []; x_array = [] #Arrays to hold the x,y value pairs to be plotted

	if first <= last:
		lower_bound_x = first - 5
		upper_bound_x = last + 5
		lower_bound_y = func.subs({variable:lower_bound_x})
		upper_bound_y = func.subs({variable:upper_bound_x})
		i = lower_bound_x

		while i <= upper_bound_x:
			x_array.append(i)
			y_array.append(func.subs({variable:i}))
			i = i + 0.05
		plt.plot(x_array, y_array, linestyle='-')
		plt.xlim(float(lower_bound_x), float(upper_bound_x))
	elif first > last:
		lower_bound_x = last - 5
		upper_bound_x = first + 5
		lower_bound_y = func.subs({variable:lower_bound_x})
		upper_bound_y = func.subs({variable:upper_bound_x})
		i = lower_bound_x

		while  i <= upper_bound_x:
			x_array.append(i)
			y_array.append(func.subs({variable:i}))
			i = i + 0.05
		plt.xlim(float(lower_bound_x), float(upper_bound_x))
		plt.plot(x_array, y_array, linestyle='-')

'''Plots the values calculated by the algorithm while trying
 to find the minimum value'''
def draw_path(x_values, y_values, min_x):
	plt.style.use('seaborn-whitegrid')
	plt.plot(x_values, y_values, 'o', markersize='2', color='red')
	plt.xlabel('x')
	plt.ylabel('f(x)')
	plt.title('Gradient Descent Algorithm')
	plt.ylim(float(min_x-100), float(min_x+100))
	plt.show()

if __name__ == '__main__':
	expr = input('Enter a function of one variable: ')
	try:
		func = sympify(expr)
	except SympifyError:
		print('Invalid function entered')
	else:
		var = input('Enter the variable: ')
		variable = Symbol(var)
		initial_value = float(input('Enter the initial value: '))
		derivative = Derivative(func, variable).doit()
		min_x, x_values, y_values = gradient_descent(initial_value, func, derivative, variable)
	
		if min_x:            
			print('{0}: {1}'.format(variable.name, min_x))            
			print('Minimum value: {0}'.format(func.subs({variable:min_x})))
			create_function_graph(x_values)
			draw_path(x_values, y_values, min_x)
		

