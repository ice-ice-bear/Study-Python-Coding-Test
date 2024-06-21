import sys
from collections import deque

sys.stdin = open('in1.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

a_list = []
l_r = []
last = 0
cnt = 0

for _ in range(n):
    if a[0] > a[-1]:
        last = a.pop()
        a_list.append(last)
        l_r.append('R')
        cnt += 1
    if a[0] < a[-1]:
        last = a.pop(0)
        a_list.append(last)
        l_r.append('L')
        cnt += 1
    if a[0] < last or a[-1] < last:
        continue


print(a_list)

for i in l_r:
    print(i, end='')
    
    