import sys
input = sys.stdin.readline

N, B = input().split() # B진법 수 N
numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = 0 
for i in range(len(N)):
    digit = N[i]
    if '0' <= digit <= '9': # 숫자인 경우
        value = int(digit)
    else: # A-Z인 경우
        value = numbers.index(digit)
    
    answer += (value * (int(B) ** (len(N) - 1 - i))) 

print(answer)