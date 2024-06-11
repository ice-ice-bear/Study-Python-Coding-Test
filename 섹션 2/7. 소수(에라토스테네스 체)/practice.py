import sys

# Redirect standard input to read from 'in2.txt'
sys.stdin = open('in2.txt', 'r')

# Read the integer n from input
n = int(input())

# Create a list 'ch' of size (n+1) initialized with zeros to track prime numbers
ch = [0]*(n+1)

# Initialize count of prime numbers
cnt = 0

# Loop from 2 to n (inclusive)
for i in range(2, n+1):
    # If 'ch[i]' is 0, it means 'i' is a prime number
    if ch[i] == 0:
        # Increment the prime count
        cnt += 1
        # Mark all multiples of 'i' as non-prime by setting 'ch[j]' to 1
        for j in range(i, n+1, i):
            ch[j] = 1

# Print the count of prime numbers
print(cnt)
