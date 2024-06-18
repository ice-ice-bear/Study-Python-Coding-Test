import sys
sys.stdin = open('in2.txt', 'r')

n = int(input())
ath = []
for i in range(n):
    ath.append(list(map(int, input().split())))

ath.sort(key=lambda x: (x[0], x[1]))

print(ath)

small = ath[0][0]
light = ath[0][1]

def samllest_lightest(small, light):
    for i in range(n):
        if ath[i][0] < small:
            small = ath[i][0]
        if ath[i][1] < light:
            light = ath[i][1]
            break
        return small, light

samllest_lightest(small, light)

cnt = 0

for height, weight in ath:
    if height > small and weight > light:
        cnt += 1 
        small = height
        light = weight

print(cnt)