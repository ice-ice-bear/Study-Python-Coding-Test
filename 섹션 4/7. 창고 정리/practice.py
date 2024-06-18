import sys
sys.stdin = open('in2.txt', 'r')

l = int(input())
wh = list(map(int, input().split()))
m = int(input())

for i in range(m):
    wh[wh.index(max(wh))] -= 1
    wh[wh.index(min(wh))] += 1

print(max(wh) - min(wh))
