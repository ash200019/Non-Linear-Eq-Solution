#Runge-Kutta Method (Order 4)



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
		m2 = func((xi + (h/2)),(yi + ((h*m1)/2)))
		m3 = func((xi + (h/2)),(yi + ((h*m2)/2)))
		m4 = func((xi + h),(yi + (m1*h)))
		
		yn = yi +((h/6)*(m1 + (2*m2) + (2*m3) + m4))
		xi = xi + h
		yi = yn
		if xi == xn:
			break
			
	print("\ny(",xn,"): ", yn)
	
if __name__ == '__main__':
	main()
