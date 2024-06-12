import sys
sys.stdin = open('in1.txt', 'r')

n = int(input())

for i in range(n):
    text = input()
    text = text.upper()
    size = len(text)
    for j in range(size//2):
        if text[j] != text[-1-j]:
            print(f'#{i+1} NO')
            break
    else: #break를 만나지 않으면 정상적으로 else를 실행
        print(f'#{i+1} YES') 