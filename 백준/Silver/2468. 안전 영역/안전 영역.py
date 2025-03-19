import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(visited, x, y, h):
    visited[x][y] = 1 # 방문 처리

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and arr[nx][ny] > h:
            dfs(visited, nx, ny, h)

max_height = 1    
for h in range(1, 101):

    visited = [[0] * N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] > h:
                count += 1
                dfs(visited, i, j, h)
    
    max_height = max(max_height, count)

print(max_height)