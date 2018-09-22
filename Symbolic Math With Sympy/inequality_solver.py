#Finds the solution to a polynomial, rational or univariate inequaltity function
#, if the solution exits

from sympy import Symbol, sympify, solveset, S

#Finds a solution to an inequality if it exits
def isolve(inequality):
	x = Symbol('x')
	inequ_obj = sympify(inequality)
	solution = solveset(inequ_obj, x, domain=S.Reals)
	print(solution)

if __name__ == '__main__':
	inequality = input("Enter the inequality: ")
	try:
		isolve(inequality)
	except Exception as e:
		print(e)



