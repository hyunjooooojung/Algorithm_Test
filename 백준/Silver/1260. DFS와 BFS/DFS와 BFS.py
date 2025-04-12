import sys
from collections import deque
input = sys.stdin.readline

def dfs(V, visited1, graph):
    visited1[V] = 1 # 방문처리
    print(V, end=" ")
    
    for i in range(1, N+1):
        if not visited1[i] and graph[V][i] == 1:
            dfs(i, visited1, graph)

def bfs(V, visited2, graph):
    visited2[V] = 1 # 방문처리
    queue = deque([V])

    while queue:
        x = queue.popleft()
        print(x, end=" ")

        for i in range(1, N+1):
            if not visited2[i] and graph[x][i] == 1:
                queue.append(i)
                visited2[i] = 1

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited1 = [0] * (N+1)
visited2 = [0] * (N+1)

dfs(V, visited1, graph)
print()
bfs(V, visited2, graph)
