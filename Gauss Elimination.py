#Basic Gauss Elimination Methods

#Name: Rejoy Chakraborty
#Sem: V 	Subject: Computer Science
#Subject: Numerical Methods (DSE-II)
#Roll No: 717

import numpy as np

def swap_row(mat,r1,r2):
	temp = mat[r1]
	mat[r1] = mat[r2]
	mat[r2] = temp
	
def normalize(mat,i):
	for j in range(i+1,len(mat)):
		fact = (mat[j][i]/mat[i][i])
		for k in range(0,len(mat)+1):
			mat[j][k] -= fact*mat[i][k]
			 	
def fwd_elimination(mat):
	n = len(mat)
	print("\n\n")
	for i in range(n-1):
		if mat[i][i] == 0:
			swap_row(mat,i,i+1)
		normalize(mat,i)
		m = np.array(mat)
		m = m[:,:n]
		if (np.linalg.det(m) == 0):
			print ("Singular Matrix!! No Unique solution Exists!!")
			return False
	return True
	
		
def print_mat(mat):
	for i in range(len(mat)):
			print(mat[i])
			print("\n")	
	
def bwd_elimination(mat):
	n = len(mat)
	x = [0]*n
	
	for i in range(n-1,-1,-1):
		x[i] = mat[i][n]
		
		for j in range(i+1,n):
			x[i] -= mat[i][j]*x[j]
			
		x[i] = x[i]/mat[i][i]
		
	print("Solution: \n\n")
	for i in range(0,n):
		print(x[i])
		 
def main():
	n = int(input("Enter the size of n of your n x n+1 augmented matrix: "))
	mat = []
	  
	print("Enter your augmented matrix row-wise: \n")  
	for i in range(n):          
		a =[] 
		for j in range(n+1): 
			a.append(float(input())) 
		mat.append(a) 
	
	print("Your input matrix: ")
	print_mat(mat)
	if(fwd_elimination(mat) == True):
		print("After Forward Elimination: ")
		print_mat(mat)
		bwd_elimination(mat)
	
if __name__ == '__main__':
	main()
	
