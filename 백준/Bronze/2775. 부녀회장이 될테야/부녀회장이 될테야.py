import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    dp = [i for i in range(1, n+1)] # 0층
    
    for i in range(k):
        for j in range(1, n):
            dp[j] += dp[j-1]
    print(dp[-1])