import sys
sys.stdin = open('in3.txt', 'r')

a = int(input())
list_a = list(map(int, input().split()))
b = int(input())
list_b = list(map(int, input().split()))

new_list = list_a + list_b
new_list.sort()

for i in range(len(new_list)):
    print(new_list[i], end=' ')
