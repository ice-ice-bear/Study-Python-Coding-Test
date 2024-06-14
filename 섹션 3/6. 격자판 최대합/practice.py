import sys
sys.stdin = open('in1.txt', 'r')  # Set up the input file to be read from

n = int(input())  # Read the value of n from the input file

# Create a 2D list 'a' that represents the grid
a = [list(map(int, input().split())) for _ in range(n)]

# Initialize variables to store the sums
row_sum = []  # List to store the sum of each row
col_sum = []  # List to store the sum of each column
l_cross_sum = 0  # Sum of the left diagonal
r_cross_sum = 0  # Sum of the right diagonal

# Iterate through each row of the grid
for i in range(n):
    # Calculate the sum of the current row and append it to row_sum
    row_sum.append(sum(a[i]))
    
    # Calculate the sum of the left diagonal
    l_cross_sum += a[i][i]
    
    # Calculate the sum of the right diagonal
    r_cross_sum += a[i][n-i-1]
    
    # Calculate the sum of the current column
    sum_col = 0
    for j in range(n):
        sum_col += a[j][i]
    # Append the column sum to the col_sum list
    col_sum.append(sum_col)

# Print the results
print(row_sum)
print(col_sum)
print(l_cross_sum)
print(r_cross_sum)
