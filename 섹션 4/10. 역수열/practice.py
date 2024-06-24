import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

rev_seq_a= list(n*[0])

for idx, num in enumerate(a):
    print(idx+1, num)
    if rev_seq_a[num-1] == 0:
        rev_seq_a[num-1] = idx+1

print(rev_seq_a)
