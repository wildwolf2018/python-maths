import csv
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet

#Reads data from a csv file
def read_file(filename):
	football = [] #Students who play football
	others = [] #Students who play other sports
	with open(filename) as cvs_file:          
		reader = csv.reader(cvs_file) 
		next(reader) 
		for row in reader:
			row_id = int(row[0])
			if int(row[1]) == 1:
		 		football.append(row_id)
			if int(row[2]) == 1:
				others.append(row_id)
	return football, others

'''Draws a venn digramm showing number of elements common to both sets
   and number of elemnets unique to each set
'''
def draw_venn(sets):
	 venn2(subsets=(sets[0], sets[1]), set_labels=('football', 'others'))
	 plt.show()

if __name__ == '__main__':
	filename = input("Enter the file name: ")
	football_set, others_set = read_file(filename)
	s1 = FiniteSet(*football_set)
	s2 = FiniteSet(*others_set)
	draw_venn([s1, s2])
