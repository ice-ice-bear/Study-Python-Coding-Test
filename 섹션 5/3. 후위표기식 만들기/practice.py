import sys
sys.stdin = open('input.txt', 'r')

a = str(input())
cal = ['+', '-', '*', '/', '(', ')']
cal_h = ['*', '/']
cal_l = ['+', '-']
stack = []
res = []

for char in a:
    if char not in cal:
        res.append(char)
    else:
        while stack and stack[-1] in cal_h:
            res.append(stack.pop())
        stack.append(char)

print(res)
print(stack)