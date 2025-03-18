import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(arr, visited, x, y, N):
    count = 1
    visited[x][y] = 1 # 방문 처리

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == 1:
            count += dfs(arr, visited, nx, ny, N) # DFS 결과 누적
    
    return count

N = int(input())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

homes = [] # 단지 내 집의 수
for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            homes.append(dfs(arr, visited, i, j, N))

print(len(homes))
homes.sort()
for home in homes:
    print(home)