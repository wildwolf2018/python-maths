#This module constains functions the plots two grphs on same axis
#and solves the two equations simultaneously

from sympy import solve, sympify, Symbol
from sympy.plotting import plot
from sympy.core.sympify import SympifyError

#Draws two graphs on the same axis
def draw_graphs(graph_one, graph_two):
	graph = plot(graph_one[0], graph_two[0], xlabel='X', ylabel='Y', xlim=(-10, 10), ylim=(-10, 10), aspect_ratio={'auto'},
		 legend=True, show=False)
	graph[0].line_color = 'b'
	graph[1].line_color = 'r'
	graph.show()


if __name__ == '__main__':
	try:
		exp1 = input("Enter first expression in terms of x and y: ")
		exp2 = input("Enter second expression in terms of x and y: ")
		equation_1 = sympify(exp1)
		equation_2 = sympify(exp2)
		
		#Rewrite equations in terms of x
		y = Symbol('y')
		equation1_in_x = solve(equation_1, y)
		equation2_in_x = solve(equation_2, y)

		#Plot the two expressions
		draw_graphs(equation1_in_x, equation2_in_x)
	
		#Solve the equations simultaneously
		answer = solve((equation_1, equation_2), dict=True)
		if len(answer) != 0:
			x = Symbol('x')
			print("Point of intersection\nX = " + str(answer[0][x]) + ", Y = " + str(answer[0][y]))
		else:
			print("Point of intersection does not exist.Therefore there's no solution.")
	except SympifyError:
		print("Invalid expression")