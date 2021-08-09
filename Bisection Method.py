#Bisection Methods


	def main():
		eq = "(x^2)-3"
		
		print ("Your Algebric/Transcendental Equation is: ",eq)
		a = int(input("Enter assumption for a: "))
		b = int(input("Enter assumption for b: "))
		
		e = int(input("Enter your approximation level i.e. upto which decimal point you want: "))
		e = 10**(-1*e)
		
		bisection(a,b,e)
		
	def bisection(a,b,e):
		
		if func(a)*func(b) >= 0:
			print("Your assumption is wrong about a and b!!")
			return
			
		c = float(a)
		iteration = 0
		
		while ((b-a) >= e):
			c = (a+b)/2
			
			if func(c) == 0.0:
				break
				
			if (func(c)*func(a) < 0):
				b = c
			elif (func(c)*func(b) < 0):
				a = c
				
			iteration += 1
		
		print("The root of the equation: ",c)
		print("Total iteration taken: ",iteration)
		
		
	def func(x):
		return (x**2) - 3
