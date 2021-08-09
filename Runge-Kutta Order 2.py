#Runge-Kutta Method (Order 2)

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-I)
#Roll No: 717

def func(x,y):
	return (x**2) + (y**2)

def main():
	x0 = float(input("Enter x_0: "))
	y0 = float(input("Enter y_0 i.e y(x_0): "))
	xn = float(input("Enter estimating point x_n: "))
	h = float(input("Enter step size: "))
	
	xi = x0
	yi = y0
	yn = 0
	while True:
		m1 = func(xi,yi)
		m2 = func((xi + ((3*h)/4)),(yi + ((3*h*m1)/2)))
		
		yn = yi +((h/3)*(m1 + (2*m2)))
		xi = xi + h
		yi = yn
		if xi == xn:
			break
			
	print("\ny(",xn,"): ", yn)
	
if __name__ == '__main__':
	main()
