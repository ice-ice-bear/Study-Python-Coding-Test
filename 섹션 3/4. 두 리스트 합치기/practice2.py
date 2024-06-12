import sys
sys.stdin = open("in2.txt", "r")

a = int(input())
list_a = list(map(int, input().split()))
b = int(input())
list_b = list(map(int, input().split()))

p1 = p2 = 0

list_c = []

while p1 < a and p2 < b:
    if list_a[p1] <= list_b[p2]:
        list_c.append(list_a[p1])
        p1 = p1 + 1
    elif list_a[p1] > list_b[p2]:
        list_c.append(list_b[p2])
        p2 = p2 + 1

for x in list_c:
    print(x, end=" ")