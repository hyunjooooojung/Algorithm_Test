import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * N # LIS
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[i], dp1[j]+1)

dp2 = [1] * N # LDS
for i in range(N-1, -1, -1): # 뒤에서부터 탐색 
    for j in range(i+1, N):
        if A[i] > A[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

max_length = 0
for i in range(N):
    max_length = max(max_length, dp1[i] + dp2[i] - 1) # 중복되는 1개 제거

# 결과 출력
print(max_length)