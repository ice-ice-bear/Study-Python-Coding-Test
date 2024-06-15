import sys
sys.stdin = open('in5.txt', 'r')

n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    if len(a[i]) == n:
        a[i].insert(0, 0)
        a[i].insert(n+1, 0)

a.insert(0, [0]*(n+2))
a.insert(n+1, [0]*(n+2))

cnt = 0

for i in range(1,n+1):
    for j in range(1, n+1):
        if a[i][j] > a[i-1][j] and a[i][j] > a[i+1][j] and a[i][j] > a[i][j-1] and a[i][j] > a[i][j+1]:
            cnt += 1
print(cnt)
            


