import sys
input = sys.stdin.readline

N = int(input().rstrip())
original_N = N
answer = 0 # 사이클

while True:
    a = N % 10 # 주어진 수의 가장 오른쪽 자리 수
    b = (N // 10) + (N % 10) # 주어진 수의 각 자리 숫자 합
    N = (a * 10) + (b % 10) # 새로운 수
    answer += 1
    
    if N == original_N:
        print(answer)
        break