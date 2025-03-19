import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

def dfs(x, y, color):
    visited[x][y] = 1 # 방문 처리
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == color:
            dfs(nx, ny, color)

sum = 0 # 적록색약이 아닌 사람이 봤을 때의 구역의 개수   
for color in ["R", "G", "B"]:
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == color:
                dfs(i, j, color)
                sum += 1

sum2 = 0 # 적록색약인 사람이 봤을 때의 구역의 수
for i in range(N):
    for j in range(N):
        if arr[i][j] == "G":
            arr[i][j] = "R"

visited = [[0] * N for _ in range(N)]
for color in ["R", "B"]:
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and arr[i][j] == color:
                dfs(i, j, color)
                sum2 += 1

print(sum, sum2)