### taylor.py: numerically solve an ODE using a Taylor Series approximation.
import math
import numpy

## Example 1: dy/dx = y - x, y(0) = 1
## y' = y-x
## y''= y' - 1
## y''' = y''

# inputs
dx = 0.1
init_x = 0.0
init_y = 2.0
final_x = 4.0

# outputs
final_y = init_y
prev_y = init_y

for i in numpy.linspace(init_x, final_x-dx, (final_x-init_x)/dx):
	final_y = prev_y + (prev_y - i)*dx/(math.factorial(1)) + (prev_y - i - 1)*(dx**2)/(math.factorial(2)) + (prev_y - i -1)*(dx**3)/(math.factorial(3))
	prev_y = final_y

print("Results:\n")
print("y({0}) = {1}".format(final_x, final_y))

# Analytical solution: y(x) = e^x + x + 1
exact = math.e**final_x + final_x + 1

print("Exact solution = {0}".format(exact))
print("Relative error = {0}%".format(100*(final_y-exact)/exact))
