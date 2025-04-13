import sys
input = sys.stdin.readline

from collections import deque

M, N = map(int, input().split()) # 가로 칸의 수 M = 열 개수 / 세로 칸의 수 N = 행 개수
tomatos = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1: # 익은 토마토
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M and tomatos[nx][ny] == 0:
            queue.append((nx, ny))
            tomatos[nx][ny] = tomatos[x][y] + 1 # 일 추가

day = 0
for tomato in tomatos:
    if 0 in tomato:
        print(-1)
        break
    else:
        day = max(day, max(tomato))
else:
    print(day - 1) # 1부터 시작했으니 -1