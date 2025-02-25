import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# LIS의 개수를 저장할 배열
dp = [1] * N # 모두 1로 설정(최소 : 각 숫자 하나만 선택하는 경우)
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))