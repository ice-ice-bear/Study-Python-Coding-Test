import sys
sys.stdin = open('in3.txt', 'r')
nums = []
a = [list(map(int, input().split())) for _ in range(7)]

cnt = 0


for i in range(7):
    for j in range(3):
        nums.append(a[i][j:j+5])
        nums.append([a[k+j][i] for k in range(5)])

cnt = 0

for i in range(len(nums)):
    if nums[i] == nums[i][::-1]:
        cnt += 1

print(cnt)








