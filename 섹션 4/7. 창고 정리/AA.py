import sys
sys.stdin = open('in1.txt', 'r')

l = int(input())
a = list(map(int, input().split()))
m = int(input())

a.sort()

for _ in range(m):
    a[0] += 1
    a[l-1] -= 1
    a.sort()

print(a[l-1] - a[0])