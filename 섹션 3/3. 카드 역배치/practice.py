import sys
sys.stdin = open('in2.txt', 'r')

num_list = []
for i in range(20):
    i = i+1
    num_list.append(i)

def reverse(num_list, x, y):
    rev_list = num_list[x-1:y]
    rev_list.reverse()
    num_list[x-1:y] = rev_list
    return num_list

for i in range(10):
    a , b = map(int, input().split())
    reverse(num_list, a, b)

for i in range(20):
    print(num_list[i], end=' ')
    
    

