"""
File: quadratic_solver.py
Name: Doris
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""

import math


def main():
	"""
	After the user entering 3 inputs,
	which are a, b, and c in the quadratic equation - ax^2 + bx + c = 0,
	the program will print out how many roots and the value of each root, using quadratic formula.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a:'))
	b = int(input('Enter b:'))
	c = int(input('Enter c:'))

	# Discriminant: b^2 - 4ac
	discriminant = (b**2)-(4*a*c)

	if a == 0:
		print('It is not the quadratic equation!')
	elif discriminant > 0:
		root1 = (-b + math.sqrt(discriminant)) / (2 * a)
		root2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print('Two roots: '+str(root1)+', '+str(root2))
	elif discriminant == 0:
		root = -b / (2 * a)
		print('One root: '+str(root))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
