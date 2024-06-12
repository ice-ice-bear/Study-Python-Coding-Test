import sys
sys.stdin = open('in2.txt', 'r')

n = int(input())

def reverse_text(text):
    return text[::-1] # 거꾸로된 문자열 출력

for i in range(n):
    text = input()
    text = text.lower()
    re_text = reverse_text(text)
    if text == re_text:
        print(f'#{i+1} YES')
    else:
        print(f'#{i+1} NO')


