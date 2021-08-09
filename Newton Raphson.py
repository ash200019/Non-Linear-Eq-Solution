#Newton Raphson Methods

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-II)
#Roll No: 717

from sympy  import *

def newton_raphson(f,f_prime,a,e):
	h = f(a)/f_prime(a)
	while abs(h) >= e:
		h = f(a)/f_prime(a)
		a = a - h
	print("The root of the equation is: ",a)

def main():
	x = Symbol('x')
	f = x**3 - x - 3
	f_prime = f.diff(x)
	
	print("Your function: ",f);
	print("Derivative of the function: ",f_prime)
	
	f = lambdify(x, f)
	f_prime = lambdify(x, f_prime)
	
	a = float(input("Enter an initial value: "))
	e = int(input("Enter the precision level: "))
	e = 10**(-1*e)
	
	newton_raphson(f,f_prime,a,e)
	
if __name__ == '__main__':
	main()
