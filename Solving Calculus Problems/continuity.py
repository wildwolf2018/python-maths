'''
Determines whether a function of a single varable
is continous at a point.
'''

'''Checks for continuity
Returns True is function is continuous, False otherwise'''
from sympy import Symbol, sympify, Limit, S

def check_continuity(function, a):
	is_continuous = False
	right_limit = Limit(f, x, a).doit()
	if right_limit != S.Infinity:
		left_limit = Limit(f, x, a, dir='-').doit()
		if left_limit != S.Infinity and left_limit == right_limit:
			f_value = f.subs({x:a})
			if f_value == left_limit:
				is_continuous = True
	return is_continuous

if __name__ == '__main__':
	expr = input('Enter a function of one variable: ')
	try:
		f = sympify(expr)
	except SympifyError:
		print('Invalid function entered')
	else:
		var = input('Enter the variable: ')
		x = Symbol(var)
		a = float(input('Enter the point to check the continuity at: '))

		if check_continuity(f, a) == True:
			print('{0} is continuous at {1}'.format(f, a))
		else:
			print('{0} is not continuous at {1}'.format(f, a))
