#Simpson's 1/3 Rule

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-I)
#Roll No: 717

import numpy as np

def func(x):
	return np.exp((-x/2))
	
def main():
	a = float(input("Enter lower limit: ")) #lower limit
	b = float(input("Enter upper limit: ")) #upper limit
	n = float(input("Enter no. of steps ")) #No. of steps	
	s = 2
	h = ((b-a)/n)/s #interval
	
	i = a
	res = 0
	while True:
		res = res +((h*(func(i) + (4*func(i+h)) + func(i+(2*h))))/3)
		i = i+(h*s)
		if i == b:
			break
				
	print("Integration value: ",res)
	
if __name__ == '__main__':
	main()
	
