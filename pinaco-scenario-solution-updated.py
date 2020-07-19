import numpy as np 	#import numpy and alias as np
R = int(input("Enter the number of rows:")) 	#Getting input for row
C = int(input("Enter the number of columns:")) 	#Getting inout for column
  

matrix = [] 	#Assigning a matrix
#print("Enter the entries rowwise:") 
  

for i in range(R):          #To get the row value through for loop
    a =[] 					#Assign a another matix for append the value
    for j in range(C):      #To get the row value through for loop
        a.append(0)			# Appending 0 to all the indices of matrix
    matrix.append(a)		# Appending the value to the original matrix
print("\nThe sturcture of the theatre :")
#print(matrix)
#print(matrix[i][j])

for i in range(R): 		
    for j in range(C): 
        print(matrix[i][j], end = " ") #Prints in the matrix form
    
    print()


def point(R,C):			# Defining a function for checking our rule for seating
	for poirow in range(R):
		for poicol in range(C):
			try:  #Checking if all the indices are zero or not
				if matrix[poirow][poicol-1]==0:
					if matrix[poirow][poicol+1]==0:
						if matrix[poirow-1][poicol]==0:
							if matrix[poirow+1][poicol]==0:
								if matrix[poirow+1][poicol+1]==0:
					 				if matrix[poirow+1][poicol-1]==0:
					 					if matrix[poirow-1][poicol-1]==0:
					 						if matrix[poirow-1][poicol+1]==0:
					 							matrix[poirow][poicol]=1 #store the value if the condition is true
				
			except IndexError: #Handling the IndexError got from the try block
				#print("\nThrough exception-1")
				if matrix[poirow-1][poicol-1]==0:
					if matrix[poirow-1][poicol]==0:
						try:
							if matrix[poirow-1][poicol+1]==0:
								matrix[poirow][poicol]=1
							
						except IndexError:
							#print("\nThrough exception-2")
							try:
								if matrix[poirow+1][poicol-1]==0:
									matrix[poirow][poicol]=1
								
							except IndexError:
								#print("\nThrough exception-3")
								matrix[poirow][poicol]=1


print("\nThe final sturcture after placing all the people:")
for i in range(R):    
	for j in range(len(matrix[0])): #Getting the length of matrix to print the final matrix structur
   		point(R,C)
   		print(matrix[i][j], end = " ")
	print()

print("\nThe maximum number of person can be seated in this theatre :")
print(np.count_nonzero(matrix)) #Gives the count of non-zero values