import sys
input = sys.stdin.readline

N = int(input())
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[-1]))