'''
Calculates the the arc beteen point A and B  along a curve
specified by the user
'''
from sympy import Derivative, Symbol, sympify, integrate, expand

if __name__ == '__main__':
	expr = input('Enter a single-variable function of x: ')
	lower_limit = float(input('Enter x coordinate of point A: '))
	upper_limit = float(input('Enter x coordinate of point B: '))
	try:
		fx = sympify(expr)
	except SympifyError:
		print('Invalid function entered')
	else:
		x = Symbol('x')
		derivative = Derivative(fx, x).doit()
		deriv_squared = expand(derivative**2)
		integrand = (1 + deriv_squared)**0.5
		result = integrate(integrand, (x, lower_limit, upper_limit)).evalf()
		print('The length of arc AB is equal to {0:.2f}'.format(result))