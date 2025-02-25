def fib_count(n):
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[i]

def fibonacci_count(n):
    return n - 2

n = int(input())
print(fib_count(n), fibonacci_count(n))