import sys
input = sys.stdin.readline

from collections import deque

def bfs(v, graph, visited):
    visited[v] = 1
    queue = deque([v])

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1

N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i, graph, visited)
        count += 1
print(count)