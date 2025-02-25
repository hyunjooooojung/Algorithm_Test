import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

dp[n-1] = triangle[n-1]
for i in range(n-2, -1, -1):
    for j in range(i+1):
        # print(i, j)
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])