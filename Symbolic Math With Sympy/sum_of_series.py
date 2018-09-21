#Sums an arbitary number of terms of a series
 
from sympy import summation, sympify, pprint, Symbol
from sympy.core.sympify import SympifyError

if __name__ == '__main__':
	try:
		nth_term = input("Enter the nth term of the series: ")
		number_of_terms = int(input("Enter the number of terms: "))
		n = Symbol('n')
		x = Symbol('x')
		formula = sympify(nth_term)
	
		#Add the terms of the series
		sum_of_series = summation(formula, (n,1, number_of_terms))
		print("Sum of {} terms of the series: ".format(number_of_terms))
		pprint(sum_of_series)
	except SympifyError:
		print("Invalid expression")