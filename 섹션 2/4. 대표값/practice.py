import sys
sys.stdin=open("in1.txt", "r", encoding="utf-8")

n = int(input())
a = list(map(int, input().split()))

find_avg = round(int(sum(a)/n), 0)

close_to_find_avg_but_large = []
close_to_find_avg_but_small = []

for i in range(len(a)):
    if a[i] > find_avg:
        close_to_find_avg_but_large.append(a[i])
    else:
        close_to_find_avg_but_small.append(a[i])

close_to_find_avg_but_large.sort()
close_to_find_avg_but_small.sort()

if a[i] == find_avg:
    closest = a[i] 
elif abs(close_to_find_avg_but_large[0] - find_avg) < abs(close_to_find_avg_but_small[0] - find_avg):
    closest = close_to_find_avg_but_large[0]
else:
    closest = close_to_find_avg_but_small[0]

for i in range(len(a)):
    if a[i] == closest:
        print(find_avg ,i+1)
        break



