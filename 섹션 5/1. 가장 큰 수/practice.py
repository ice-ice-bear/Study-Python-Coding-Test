import sys
sys.stdin = open('input.txt', 'rt')

num, m = map(int, input().split())
num = list(map(int, str(num)))
stack = []
for x in num:
    # 스택이 비어있지 않은경우, m이 0보단 큰 경우, 스택의 마지막 자료가 나보다 작은 경우
    while stack and m > 0 and stack[-1] < x: 
        stack.pop()
        m -= 1
    stack.append(x)
 
print(stack)