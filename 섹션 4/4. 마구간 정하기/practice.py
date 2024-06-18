import sys
sys.stdin = open('in3.txt', 'r')

n, c = map(int, input().split())

barn = []
for i in range(n):
    a = int(input())
    barn.append(a)

barn.sort()

lt = barn[0]
rt = barn[-1]
mid = lt + rt //2
res = 0

def num_barn(dist):
    cnt = 1
    ep = barn[0]
    for i in range(1, n):
        if barn[i] - ep >= dist:
            cnt += 1
            ep = barn[i]
    return cnt

while lt <= rt:
    mid = (lt + rt) // 2
    if num_barn(mid) >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)








