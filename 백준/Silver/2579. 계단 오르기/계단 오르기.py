import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for i in range(1, n+1)]

if n < 2:
    print(stairs[n])
else:
    dp = [0] * 301
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]
    for i in range(3, n+1):
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(dp[n])