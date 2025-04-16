import sys
input = sys.stdin.readline

strings = input().strip()
dp = [0] * 26
for s in strings:
    dp[ord(s) - 97] += 1
print(*dp)