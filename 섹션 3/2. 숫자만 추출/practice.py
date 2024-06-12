import sys
sys.stdin = open('in2.txt', 'r')

# is_digit: 지수가 붙은 숫자도 인식 
# is_decimal: 0~9까지의 숫자만 인식

text = input()

def extract_num(text):
    num = ''
    for s in text:
        if s.isdigit():
            num += s
            # num = num*10+int(s)
    return int(num)

extract_num(text)
print(extract_num(text))

def find_divisions(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    return cnt

print(find_divisions(extract_num(text)))