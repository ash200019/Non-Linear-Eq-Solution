#Simpson's 1/3 Rule



import numpy as np

def func(x):
	return (x**3) + 1
	
def main():
	a = float(input("Enter lower limit: ")) #lower limit
	b = float(input("Enter upper limit: ")) #upper limit
	n = 3 #No. of steps	
	h = ((b-a)/n) #interval
	
	res = ((3*h)/8)*(func(a) + 3*(func(a+h) + func(a+(2*h))) + func(a+(3*h)))
			
	print("Integration value: ",res)
	
if __name__ == '__main__':
	main()
	

