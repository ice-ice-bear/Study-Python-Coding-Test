import sys
sys.stdin = open('in1.txt', 'r')

n = int(input())
a = list(map(int, input().split()))

rev_seq_a= list(n*[0])

def check_0(a, num):
    cnt = 0
    for i in range(num):
        if a[i] == 0:
            cnt += 1
    return cnt


def next_0(a, num):
    cnt = 0
    for i in range(len(a)):
        if a[i] == 0:
           cnt += 1
           if cnt == num + 1:
               return i 

for idx, num in enumerate(a):
    idx = idx + 1
    if rev_seq_a[num] == 0:        
        if check_0(rev_seq_a, num) == num:
            rev_seq_a[num] = idx
        else:
            index = next_0(rev_seq_a, num)
            rev_seq_a[index] = idx
    


print(rev_seq_a)
