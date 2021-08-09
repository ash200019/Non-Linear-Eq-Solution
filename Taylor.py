#Taylor Series (Upto 3rd Order Derivative)



import math as m

def func_d1(x,y):
	return x+y+(x*y) 
	
def func_d2(x,y):
	return ((1+x)*func_d1(x,y)) + y + 1
	
def func_d3(x,y):
	return ((x+1)*func_d2(x,y)) + (2*func_d1(x,y))

def main():
	x0 = float(input("Enter x_0: "))
	y0 = float(input("Enter y_0 i.e y(x_0): "))
	xn = float(input("Enter estimating point x_n: "))
	
	yn = y0 + ((xn - x0)*func_d1(x0,y0)) + ((((xn - x0)**2)*func_d2(x0,y0))/m.factorial(2)) + ((((xn - x0)**3)*func_d3(x0,y0))/m.factorial(3))
	
	print("\ny(",xn,"): ", yn)
	
if __name__ == '__main__':
	main()

	
	
	
