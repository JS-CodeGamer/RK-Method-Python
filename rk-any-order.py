#!/usr/bin/python3
# Python program to implement Runge Kutta method
import sys
# Python program to implement Runge Kutta method
# A sample differential equation "dy / dx = (x - y)/2"
def dydx(x, y):
	return ((x - y)/2)

# Finds value of y for a given x using step size h
# and initial value y0 at x0.
def rungeKutta(initial_x, initial_y, final_x, step, stages):

	# Count number of iterations using step size or
	# step height h
	n = (int)((final_x - initial_x)/step)
	x0 = initial_x
	x = final_y

	# Iterate for number of iterations
	y = initial_y
	k = []

	print("For your stages input a[i][j]."
	print("For refernce, see https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#Explicit_Runge%E2%80%93Kutta_methods")

	a = []
	for stage in range(stages):
		buffer = []
		for stage_index in range(stage):
			buffer.append( float( input("Input a[{stage}][{stage_index}]") ) )
		a.append(buffer)
		del buffer

	# Note: other implimentations of RK method may use any method to generate c's.
	#   Only requisite for an rk method to work is sum(b[i]) = 1 and substituition
	#      result should be as close to taylor series as possible
	c = [ c.append(sum(a[stage])) for stage in range(stages) ]

	# TODO: Generate b such that b[mid +1] = b[mid -1] = b[mid]/2 and sum(b[i])=1
	# a a/2 a/2 a/4 a/4 a/8 a/8 ... 
	#b = []
	#for stage in range(stages):
		#buffer = 0.0
		#b[i] =

	for i1 in range(n):
		# Apply Runge Kutta Formulas to find next value of y
		for stage in range(stages):
			buffer = 0.0
			for stage_index in range(stage):
				buffer +=  a[stage][stage_index] * k[stage_index]
			k.append( h * dydx(x + c[stage] * h, y + buffer) )
			del buffer

		# Update next value of y
		for stage in range(stages):
			y += b[stage] * k[stage]

		# Update next value of x
		x0 = x0 + h
	return y

# Driver method
x0 = float(input("Input starting value of x(x0): "))
y0 = float(input("Input starting value of y(y0): "))
x = float(input("Input ending value of x (x): "))
h = float(input("Input value of step size (h):  "))
stages = float(input("Input the stages you want to use: ")
print ( 'The value of y at x is:', rungeKutta(x0, y0, x, h, stages) )


# #------------------------------------------------------------------
# # Instruction for input:
#     print("Enter equation in terms of dy/dx.")
#     print()
#     print("Note: your expression must not contain anything else")
#     print("than x, y, (+), (-), (*), (/), 0-9 or pi or e.")
#     print("All implemented checks are case sensitive.")
#     print("If you require power use (**) instead of (^).")
#     print("Eg. for equation: dy/dx = x-(y^2) enter x-y**2.")
#     print()
#     print("Funtionality to include differntial terms in equaions"
#     print("needs to be implimented, also functionality to include"
#     print("brackets is not implemented.")
#     str_eqn = input("Enter Equation: ")
