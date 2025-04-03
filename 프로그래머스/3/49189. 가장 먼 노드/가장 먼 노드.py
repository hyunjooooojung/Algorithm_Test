from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [0] * (n+1)
    visited[1] = 1
    distance = [0] * (n+1)
    queue = deque([1]) # 1번 노드부터 시작
    
    while queue:
        now = queue.popleft()
        
        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                distance[neighbor] = distance[now] + 1
                queue.append(neighbor)
    
    return distance.count(max(distance))