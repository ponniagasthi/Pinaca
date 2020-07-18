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
print(matrix)
#print(matrix[i][j])

for i in range(R): 		
    for j in range(C): 
        print(matrix[i][j], end = " ") #Prints in the matrix form
    
    print()

def point():				# Defining a function for checking our rule for seating
	poirow =int(input("\nEnter a position where a person can sit (row) :"))
	poicol =int(input("Enter a position where a person can sit (column) :"))
	#poirowmax = len(poirow)
	#poicolmax = len(poicol)
	
	print(matrix[poirow][poicol])

	#print("below",matrix[poirow+1][poicol])
	#print("top",matrix[poirow-1][poicol])
	#print("right",matrix[poirow][poicol+1])
	#print("left",matrix[poirow][poicol-1])
	#print("diagonal-down-right",matrix[poirow+1][poicol+1])
	#print("diagonal-down-left",matrix[poirow+1][poicol-1])
	#print("diagonal-top-left",matrix[poirow-1][poicol-1])
	#print("diagonal-top-right",matrix[poirow-1][poicol+1])
	#if matrix[poirow][poicol-1]==0 and matrix[poirow][poicol+1]==0:
	#if matrix[poirow+1][poicol]==0 and matrix[poirow-1][poicol]==0 and matrix[poirow][poicol+1]==0 and matrix[poirow][poicol-1]==0  and matrix[poirow+1][poicol+1]==0 and matrix[poirow+1][poicol-1]==0 and matrix[poirow-1][poicol-1]==0 and matrix[poirow-1][poicol+1]==0:
		
	try:  #Checking if all the indices are zero or not
		if matrix[poirow][poicol-1]==0:
			if matrix[poirow][poicol+1]==0:
				if matrix[poirow-1][poicol]==0:
					if matrix[poirow+1][poicol]==0:
						if matrix[poirow+1][poicol+1]==0:
				 			if matrix[poirow+1][poicol-1]==0:
				 				if matrix[poirow-1][poicol-1]==0:
				 					if matrix[poirow-1][poicol+1]==0:
				 						matrix[poirow][poicol]=int(input("\nSeat the person - Enter the value : ")) #store the value if the condition is true
		else:print("\n!!!According to our rule the person cannot be seated here")
		 						
	except IndexError: #Handling the IndexError got from the try block
		#print("\nThrough exception-1")
		if matrix[poirow-1][poicol-1]==0:
			if matrix[poirow-1][poicol]==0:
				try:
					if matrix[poirow-1][poicol+1]==0:
						matrix[poirow][poicol]=int(input("\nSeat the person - Enter the value : "))
					else:
						print("\n!!!According to our rule the person cannot be seated here")
				except IndexError:
					#print("\nThrough exception-2")
					try:
						if matrix[poirow+1][poicol-1]==0:
							matrix[poirow][poicol]=int(input("\nSeat the person - Enter the value : "))
						else:
							print("\n!!!According to our rule the person cannot be seated here")
					except IndexError:
						#print("\nThrough exception-3")
						matrix[poirow][poicol]=int(input("\nSeat the person - Enter the value : "))
	
			else:print("\n!!!According to our rule the person cannot be seated here")
		else:print("\n!!!According to our rule the person cannot be seated here")
	

	
	print("\nThe sturcture of the theatre after the attempt:")
	print(matrix)
	#print("3According to our rule the person cannot be seated here")
#point()
for i in range(R):    
# iterate through columns 
   for j in range(len(matrix[0])): #Getting the length of matrix to print the final matrix structur
   		point()
print("\nThe final sturcture after placing all the people:")
print(matrix)
print("\nThe maximum number of person can be seated in this theatre :")
print(np.count_nonzero(matrix)) #Gives the count of non-zero values