import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

# 이동 방향
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(graph, x, y, visited):
    global count
    visited[x][y] = True
    for i in range(4):
        x_ = x + dx[i]
        y_ = y + dy[i]
        if graph[x_][y_] and not visited[x_][y_]:
            dfs(graph, x_, y_, visited)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split()) # 배추밭 가로 M, 세로 N, 배추 개수 K
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    # 1. 그래프 정보 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y+1][X+1] = True

    # 2. 방문하지 않은 지점부터 dfs 돌기
    count = 0 # 배추 구역 개수(=필요한 지렁이 수)
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j] and not visited[i][j]:
                dfs(graph, i, j, visited)
                count += 1
    
    print(count)