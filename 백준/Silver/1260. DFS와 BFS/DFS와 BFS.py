import sys
from collections import deque

# DFS 함수 (재귀)
def dfs(graph, v, visited):
    visited.append(v)
    for i in sorted(graph[v]): # 작은 번호부터 방문
        if i not in visited:
            dfs(graph, i, visited)

# BFS 함수 (큐 사용)
def bfs(graph, start):
    visited = [] # 방문한 노드 기록
    queue = deque([start]) # 큐 초기화

    while queue:
        v = queue.popleft() # 큐에서 하나 꺼냄
        if v not in visited:
            visited.append(v) # 방문 처리
            queue.extend(sorted(graph[v])) # 방문할 노드 추가 (작은 번호부터)

    return visited

N, M, V = map(int, sys.stdin.readline().split()) # 정점 개수 N, 간선 개수 M, 탐색 시작 정점 번호 V
graph = {i: [] for i in range(1, N + 1)} 

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x) # 양방향 그래프

# DFS 실행
dfs_visited = []
dfs(graph, V, dfs_visited)

# BFS 실행
bfs_visited = bfs(graph, V)

# 결과 출력
print(" ".join(map(str, dfs_visited)))  # DFS 결과 출력
print(" ".join(map(str, bfs_visited)))  # BFS 결과 출력