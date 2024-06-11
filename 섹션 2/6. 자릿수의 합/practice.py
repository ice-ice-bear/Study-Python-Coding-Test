import sys
sys.stdin = open('in5.txt', 'r')

N = int(input())
a = list(map(int, input().split()))

numbers = []

def digit_sum(N):
    for i in range(N):
        sum = 0
        a[i] =  str(a[i])
        for j in range(len(a[i])):
            sum += int(a[i][j])
        numbers.append(sum)
     
    return a[numbers.index(max(numbers))]

print(digit_sum(N))