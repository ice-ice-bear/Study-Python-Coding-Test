import sys
sys.stdin = open('in1.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
s = e = n//2

for i in range(n):
    res += sum(a[i][s:e+1])
    if i < n//2:
        s -= 1
        e += 1 
        # res를 if 절 안에 넣고, i <= n//2를 적용하는 경우, s와 e의 계산이 한번더 들어가게 된다
        # 예) i = 3 e = 6 -> 7, s = 0 -> -1
        # 이대로 동일하게 아래에서 적용되어 i=4인 경우, e = 6 s = 0 이되는 것이다 
    else:
        s += 1
        e -= 1
        

print(res)