def dfs(computers, visited, v):
    visited[v] = 1
    
    for i in range(len(computers)):
        if not visited[i] and v != i and computers[v][i] == 1:
            dfs(computers, visited, i)
            
def solution(n, computers):
    answer = 0 # 네트워크 개수
    visited = [0] * (n+1)
    
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1
    
    return answer