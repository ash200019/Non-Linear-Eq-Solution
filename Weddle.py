#Simpson's 1/3 Rule

t: Numerical Methods (DSE-I)
#Roll No: 717

def func(x):
	return 1/(1+(x**2))
	
def main():
	a = float(input("Enter lower limit: ")) #lower limit
	b = float(input("Enter upper limit: ")) #upper limit
	n = float(input("Enter no. of steps ")) #No. of steps
	s = 6 	
	h = ((b-a)/n)/s #interval
	
	i = a
	res = 0
	while True:
		f0 = func(i)
		f1 = func(i + h)
		f2 = func(i+(2*h))
		f3 = func(i+(3*h))
		f4 = func(i+(4*h))
		f5 = func(i+(5*h))
		f6 = func(i+(6*h))
	
		res = res + (((3*h)/10)*(f0 + (5*f1) + f2 + (6*f3) + f4 + (5*f5) + f6))
		i = i+(h*s)
		if i == b:
			break
		
				
	print("Integration value: ",res)
	
if __name__ == '__main__':
	main()
	

