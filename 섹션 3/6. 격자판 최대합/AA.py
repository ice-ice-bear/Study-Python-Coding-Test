import sys
# Open the input file 'in1.txt' for reading
sys.stdin = open('in1.txt', 'r')

# Read the first line of input, which contains the value of n
n = int(input())

# Create a 2D list 'a' by reading n lines of input, where each line contains n space-separated integers
a = [list(map(int, input().split())) for _ in range(n)]

# Initialize the 'largest' variable to a very small value
largest = -2147000000

# Iterate through the rows of the 2D list 'a'
for i in range(n):
    # Initialize the sum of the elements in the current row and column to 0
    sum1 = sum2 = 0
    # Iterate through the columns of the current row
    for j in range(n):
        # Add the element at (i, j) to sum1
        sum1 += a[i][j]
        # Add the element at (j, i) to sum2
        sum2 += a[j][i]
    # Update the 'largest' variable if the current row sum is greater than the current largest value
    if sum1 > largest:
        largest = sum1
    # Update the 'largest' variable if the current column sum is greater than the current largest value
    if sum2 > largest:
        largest = sum2
    
# Reset the sum1 and sum2 variables to 0
sum1 = sum2 = 0
# Iterate through the diagonal elements of the 2D list 'a'
for i in range(n):
    # Add the element at (i, i) to sum1
    sum1 += a[i][i]
    # Add the element at (i, n-i-1) to sum2 (this is the other diagonal)
    sum2 += a[i][n-i-1]
# Update the 'largest' variable if the current diagonal sum is greater than the current largest value
if sum1 > largest:
    largest = sum1
# Update the 'largest' variable if the current other diagonal sum is greater than the current largest value
if sum2 > largest:
    largest = sum2

# Print the final value of 'largest'
print(largest)
