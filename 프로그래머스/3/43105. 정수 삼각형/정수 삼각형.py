def solution(triangle):
    answer = 0
    n = len(triangle)
    
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[-1] = triangle[-1] # 맨 마지막 열 동일하게 설정
    
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    
    answer = dp[0][0]
    return answer