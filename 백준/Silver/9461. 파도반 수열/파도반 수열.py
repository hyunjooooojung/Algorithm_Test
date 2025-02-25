def P(n):
    dp = [0] * 101
    dp[1] = dp[2] = dp[3] = 1
    dp[4] = dp[5] = 2
    for i in range(6, n+1):
        dp[i] = dp[i-2] + dp[i-3]
    
    return dp[n]
    
T = int(input())

for _ in range(T):
    N = int(input())
    print(P(N))