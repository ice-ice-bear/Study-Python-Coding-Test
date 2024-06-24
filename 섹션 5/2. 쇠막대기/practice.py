import sys
sys.stdin = open('input.txt', 'r')

a = input()

stack = []
sum = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
    else:
        # 레이저
        if a[i-1] == '(':
            stack.pop()
            sum += len(stack)
        # 선반의 끝 
        else:
            stack.pop()
            sum += 1

print(sum)