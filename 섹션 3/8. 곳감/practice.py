import sys
sys.stdin = open('in2.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


m = int(input())
# for i in range(m):
#     row_num, r_l, num_block = map(int, input().split())

#     left_block = num_block + 1
#     right_block = num_block
#     if r_l == 0:
#         a[row_num-1] = a[row_num-1][-left_block:] + a[row_num-1][:-left_block]
#     else:
#         a[row_num-1] = a[row_num-1][-right_block:] + a[row_num-1][:-right_block]

# for i in range(n):
#     print(a[i])
for i in range(m):
    row_num, r_l, num_block = map(int, input().split())
    row_num -= 1  # Adjust the index to start from 0
    if num_block > m:
        num_block = num_block - m
    if r_l == 0:  # Rotate left
        a[row_num] = a[row_num][-(num_block-1):] + a[row_num][:(num_block)]
    else:  # Rotate right
        a[row_num] = a[row_num][-num_block:] + a[row_num][:num_block-1]

for i in range(n):
    print(a[i])

res = 0
s = 0
e = n - 1
for i in range(n):
    res += sum(a[i][s:e+1])
    if i < n // 2:  
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)


