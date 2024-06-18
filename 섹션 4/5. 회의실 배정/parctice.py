import sys
sys.stdin = open('in1.txt', 'r')

n = int(input())

meeting = []

for i in range(n):
    start, end = list(map(int, input().split()))
    meeting.append((start, end))

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

print(meeting)

cnt = 0
end_time = 0

for start, end in meeting:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)