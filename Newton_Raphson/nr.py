# nr.py: A Newton-Raphson solver.
__author__  = 'Ken Newcomb'

tolerance = 1e-8

def iterate(x_prev):
	return x_prev - f(x_prev)/dfdx(x_prev) 

def f(x):
	return 4*x**3 - 8.72*x**2 + 8.72*x - 2.18

def dfdx(x):
	return 12*x**2 - 17.44*x + 17.44

# an example from "Molecular Thermodynamics" by Donald A. McQuarrie
# f(x) = 4x**3 - 8.72x**2 + 8.72*x - 2.18 = 0

# Start with an initial guess, generate first value
guess = 0.250
# Iterate and hopefully find solution.
iterations = 0
while(abs(f(guess)) > tolerance):
	iterations += 1
	print("Iteration: {0}, x = {1}, f(x) = {2}".format(iterations, guess, f(guess)))
	guess = iterate(guess)	
print("Converged Solution: {0}".format(guess))
