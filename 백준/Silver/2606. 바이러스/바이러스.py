N = int(input()) # 컴퓨터의 수
M = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

def dfs(graph, v, visited):
    global count
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)
            count += 1 # 바이러스 걸린 컴퓨터 수 + 1

graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a) 

count = 0 # 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수
visited = [False for _ in range(N+1)]
dfs(graph, 1, visited) # 1번 컴퓨터부터 바이러스 시작
print(count)