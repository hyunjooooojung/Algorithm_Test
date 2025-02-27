import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 이동 방향(8방향 (상, 하, 좌, 우 + 대각선 4방향))
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

def dfs(graph, x, y):
    graph[x][y] = False
    for i in range(8): # 가로, 세로, 대각선 방향으로 탐색
        x_ = x + dx[i]
        y_ = y + dy[i]
        # 범위 체크 + 육지(1)일 경우 DFS 호출
        if 0 <= x_ < h and 0 <= y_ < w and graph[x_][y_]:
            dfs(graph, x_, y_)

while True:
    w, h = map(int, input().split())
    if w == h == 0: # 종료조건
        break

    # 지도 그래프 할당
    graph = [list(map(int, input().split())) for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == True:
                count += 1
                dfs(graph, i, j)

    print(count)