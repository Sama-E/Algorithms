# You're given a 2D array of integers, a matrix. Write a function that returns
# the transpose of the matrix. The transpose of a matrix is a flipped 
# version of the original matric across its main diagonal (which runs
# from top-left to bottom-right); its switches the row and column indicies
# of the original matrix.

# You can assume the input matrix always has at least 1 value; however its 
# width and height are not necessaily the same.

matrix = [
  [1,2],
]

output = [
  [1],
  [2]
]

matrix1 = [
	[1,2],
	[3,4],
	[5,6]
]

output1 = [
	[1,3,5],
	[2,4,6]
]

matrix2 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

output2 = [
	[1,4,7],
	[2,5,8],
	[3,6,9]
]


# Swapping
# 1. Initialize new output matrix
# 2. Loop through the length of matrix starting with the first row
# 3. Initialize new row of new output matrix
# 4. Loop through the elements for the length of the matrix
# 5. Add to new row i, switch [col][row] to the matrix[row][col]
# 6. Add new row i to output matrix
# 7. When length of matrix(col) reached move to next row
# 8. Move step 2 then repeat step 4.
# 9. Return ouput 


# O(col*row) TimeSpace | col = width of matrix, row = height of matrix
def transposeMatrix(matrix):
	# Initialize new matrix, output
	output = []

	# For each col in the range of the length of matrix[0]
	# matrix[0] = row
	for col in range(len(matrix[0])):
		# New Row i = []
		i = []
		# For each row in the range of the length of the matrix
		for row in range(len(matrix)):
			# Add to new row i = matrix[row][col]
			i.append(matrix[row][col])
		# Add new row i to new matrix(output)
		output.append(i)
	# Return output
	return output;


print(transposeMatrix(matrix))
print(transposeMatrix(matrix1))
print(transposeMatrix(matrix2))