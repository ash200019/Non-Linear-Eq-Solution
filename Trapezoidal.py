#Trapezoidal Rule

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-I)
#Roll No: 717

import numpy as np

def func(x):
	return np.exp(x)

def main():
	a = float(input("Enter lower limit: ")) #lower limit
	b = float(input("Enter upper limit: ")) #upper limit
	n = float(input("Enter no. of steps ")) #No. of steps	
	h = (b-a)/n #interval
	
	i = a
	res = 0
	while True:
		res = res +((h*(func(i) + func(i+h)))/2)
		i = i+h
		if i == b:
			break
			
	print("Integration value: ",res)
	
if __name__ == '__main__':
	main()
	
