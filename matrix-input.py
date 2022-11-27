# For matrix input
Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
  
# Initializing the matrix  
example_matrix = []  
  
# taking RowsxColumns matrix from the user  
for i in range(Rows):  
    # taking input for the row from the user  
    single_row = list(map(int, input().split()))  
    # appending the 'single_row' to the 'example_matrix'  
    example_matrix.append(single_row)  
# printing the matrix given by user  
print(example_matrix)
