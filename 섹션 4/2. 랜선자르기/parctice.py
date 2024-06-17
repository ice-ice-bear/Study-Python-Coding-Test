import sys
sys.stdin = open('in3.txt', 'r')

k, n = map(int, input().split())

lan=[]
largest=0
for i in range(k):
    tmp=int(input())
    lan.append(tmp)
    largest=max(largest, tmp)

lan.sort(reverse= True)

def count_div_lan(lan, length):
    cnt = 0
    for i in lan:
        cnt += i//length
    return cnt

while count_div_lan(lan, largest) < n:
    largest = largest//2
    count_div_lan(lan, largest)
    if count_div_lan(lan, largest) == n:
        break

while count_div_lan(lan, largest) >= n:
    largest += 1
    count_div_lan(lan, largest)
    if count_div_lan(lan, largest) < n:
        largest -= 1
        break

print(largest)





        




