import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v) # 무방향 그래프
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if visited[i] == False:
        count += 1
        dfs(graph, i, visited) 

print(count)