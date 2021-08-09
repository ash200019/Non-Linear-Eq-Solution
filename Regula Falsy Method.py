#Regula Falsy Methods

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-II)
#Roll No: 717

def main():
	eq = "3x^2 + 6x - 45"
	
	print ("Your Algebric/Transcendental Equation is: ",eq)
	a = float(input("Enter assumption for a: "))
	print("a: ",a)
	b = float(input("Enter assumption for b: "))
	print("b:",b)
	
	e = int(input("Enter your approximation level i.e. upto which decimal point you want: "))
	e = 10**(-1*e)
	
	regula_falsy(a,b,e)
	
def regula_falsy(a,b,e):
	
	if func(a)*func(b) >= 0:
		print("Your assumption is wrong about a and b!!")
		return
		
	c = float(a)
	iteration = 1
	
	while ((b-a) >= e):
		c = b - ((func(b)*(b-a))/(func(b)-func(a)))	
		
		if func(c) == 0.0:
			break
			
		if (func(c)*func(a) < 0):
			b = c
		elif (func(c)*func(a) > 0):
			a = c
			
		iteration += 1
	
	print("The root of the equation: ",c)
	print("Total iteration taken: ",iteration)
	
	
def func(x):
	return (3*(x**2)) + (6*x) - 45
	
if __name__ == '__main__':
	main()
