#Regula Falsy Methods

from sympy import *

def main():
	eq = "4x^3 - 2x - 6"
	x = Symbol('x')
	f = (4 * x**3) - (2*x) - 6
	f = lambdify(x, f)
	
	print ("Your Algebric/Transcendental Equation is: ",eq)
	a = float(input("Enter any for a: "))
	print("a: ",a)
	b = float(input("Enter any for b: "))
	print("b:",b)
	
	e = int(input("Enter the number of iteration: "))
	
	secant(f,a,b,e)
	
def secant(f,a,b,e):
	c = float(a)
	iteration = 0
	while (iteration <= e):
		c = b - ((f(b)*(b-a))/(f(b)-f(a)))
		a = b
		b = c	
		iteration += 1
	
	print("The root of the equation (appx.): ",c)
	
if __name__ == '__main__':
	main()
