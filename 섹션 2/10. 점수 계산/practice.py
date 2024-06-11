import sys
sys.stdin = open('in3.txt', 'r')

num = int(input())

a = list(map(int, input().split()))

print(a)

point = []


for i in range(num):
    point.append(0)
    if a[i] == 1 and a[i] == a[i-1]:
        point[i] = point[i-1] + 1
    elif a[i] == 1:
        point[i] = 1
    else:
        point[i] = 0

print(point)
print(sum(point)) 