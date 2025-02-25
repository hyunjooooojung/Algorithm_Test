import sys

N = int(sys.stdin.readline()) # 2 ≤ N ≤ 1,000

# # dp[i][j]: i번째 집을 j색(빨강=0, 초록=1, 파랑=2)으로 칠했을 때 최소 비용
dp = [[0 for _ in range(3)] for _ in range(N)] 
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp[0] = costs[0][:] # 초기값 설정 - 첫 번째 집의 비용

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0] # 빨강
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1] # 초록
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2] # 파랑

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2]))