import sys
input = sys.stdin.readline

from collections import deque

def bfs(i, j):
    visited[i][j] = 1 # 방문처리
    queue = deque([(i, j)])

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    
    return visited[N-1][M-1] # 도착지점

N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * (M+1) for _ in range(N)]

print(bfs(0, 0)) # (1, 1)부터 (N, M)까지