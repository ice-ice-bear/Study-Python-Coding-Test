import sys
sys.stdin = open('in5.txt', 'r')

rot = int(input())

prize = []

for i in range(rot):
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] == a[2]:   
        prize.append(10000+ a[0]*1000)
    elif a[0] == a[1] or a[1] == a[2]:
        prize.append(1000 + a[1]*100)
    else:
        prize.append(max(a)*100)

print(max(prize))