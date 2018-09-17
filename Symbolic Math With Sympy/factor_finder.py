#finds factors of expession input by user
#throws an exception if invalid expression is entered

from sympy import factor, sympify, pprint
from sympy.core.sympify import SympifyError

if __name__ == '__main__':
	try:
		exp = input("Enter a mathematical expression: ")
		exp = sympify(exp)
		factors = factor(exp)
		pprint(factors)
	except SympifyError:
		print("Invalid expression")