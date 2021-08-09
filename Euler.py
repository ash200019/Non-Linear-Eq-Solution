#Euler's Method

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-I)
#Roll No: 717

def func(x,y):
	return (3*(x**2)) + 1

def main():
	x0 = float(input("Enter x_0: "))
	y0 = float(input("Enter y_0 i.e y(x_0): "))
	xn = float(input("Enter estimating point x_n: "))
	h = float(input("Enter step size: "))
	 
	xi = x0
	yi = y0
	yn = 0
	while True:
		yn = yi + (h*func(xi,yi))
		xi = xi + h
		yi = yn
		if xi == xn:
			break
			 
	print("\ny(",xn,"): ", yn)
	
if __name__ == '__main__':
	main()
