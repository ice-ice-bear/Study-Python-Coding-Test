import sys
sys.stdin = open('in1.txt')

n, m = map(int, input().split())

sum_dice = []

for i in range(n):
    i = i+1
    for j in range(m):
        j = j+1
        sum_dice.append(i+j)

sum_dice.sort()

num_counts= {}
for num in sum_dice:
    if num in num_counts:
        num_counts[num] += 1
    else:
        num_counts[num] = 1

max_counts = max(num_counts.values())
max_numbers = []

for num, count in num_counts.items():
    if count == max_counts:
        max_numbers.append(num)

print(max_numbers)

