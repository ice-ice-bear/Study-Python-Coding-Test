import sys
sys.stdin = open('in2.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

cnt = 0

while a:
    if len(a) ==1:
        cnt += 1
        break
    if a[0] + a[-1] <= m:
        cnt += 1
        a.pop(0)
        a.pop(-1)
    else:
        a.pop(-1)
        cnt += 1

print(cnt)
