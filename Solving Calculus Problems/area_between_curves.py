
'''
Calculates the enclosed area btween two single variable functions
'''

from sympy import Symbol, sympify, integrate

if __name__ == '__main__':
	expr = input('Enter an upper single-variable function of x: ')
	expr_2 = input('Enter a lower single-variable function of x: ')
	lower_limit = float(input('Enter the lower limit value: '))
	upper_limit = float(input('Enter the upper limit value: '))
	try:
		fx = sympify(expr)
		gx = sympify(expr_2)
	except SympifyError:
		print('Invalid function entered')
	else:
		x = Symbol('x')
		diff = integrate(fx - gx, (x, lower_limit, upper_limit))
		print('The enclosed area between f(x) = {0} and g(x) = {1} from {2} to {3} is equal to {4:.2f}'.format(fx, gx, 
			lower_limit, upper_limit, diff))
