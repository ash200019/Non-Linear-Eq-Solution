import numpy as np

def main():
	x = np.array([1,2,3])
	f = np.array([1,1,2])
	
	x_u = 2.5
	h1 = x[1] - x[0]
	h2 = x[2] - x[1]
	
	a1 = ((((f[2] - f[1])/h2) - ((f[1] - f[0])/h1))*6)/(2*(h1+h2))
	u = np.array([x_u - x[0],x_u - x[1],x_u - x[2]])
	
	if x[0] <= x_u and x_u <= x[1]:
		s1 = (a1/6*h1)*(u[0]**3 - (h1**2)*u[0]) + ((1/h1)*(f[1]*u[0] - f[0]*u[1]))
		print("Estimated value for ",x_u," is: ",s1)
	else:
		s2 = ((a1/6*h2)*((h2**2)*u[2] - u[2]**3)) + ((1/h2)*(f[2]*u[1] - f[1]*u[2]))
		print("Estimated value for ",x_u," is: ",s2)
		
if __name__ == '__main__':
	main()
