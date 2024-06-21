import sys
from collections import deque

sys.stdin = open('in1.txt', 'r')

n, m = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
p= deque(p)
cnt=0

while p:
    if len(p) == 1:
        cnt +=1
        break
    if p[0] + p[-1] > m:
        cnt += 1
    else:
        p.popleft()
        p.pop()
        cnt += 1

print(cnt)