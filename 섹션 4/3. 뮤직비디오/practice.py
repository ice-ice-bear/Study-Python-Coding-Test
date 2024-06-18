import sys
sys.stdin = open('in2.txt', 'r')

n, m = map(int, input().split())

song = list(map(int, input().split()))

def count_song(num):
    cnt=1
    sum=0
    for x in song:
        if sum+x>num:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt

lt = 1
rt = sum(song)
maxx = max(song)

while lt<=rt:
    mid=(lt+rt)//2
    if mid>=maxx and count_song(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)








