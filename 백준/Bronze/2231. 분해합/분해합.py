import sys
input = sys.stdin.readline

N = int(input())

answer = 0
for i in range(1, N+1):
    answer = i + sum(list(map(int, str(i)))) # 분해합
    if answer == N:
        print(i)
        break
    if i == N:
        print(0)