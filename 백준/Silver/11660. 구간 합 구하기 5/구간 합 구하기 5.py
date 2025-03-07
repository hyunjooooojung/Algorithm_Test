import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [list(map(int, input().split())) for _ in range(N)]
prefix = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        # 현재 위치 (i, j)의 값 = 현재 칸의 값 + 위쪽 누적합 + 왼쪽 누적합 - 중복된 대각선 값
        prefix[i][j] = numbers[i-1][j-1] + prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1]

# S(x1,y1,x2,y2)=prefix[x2][y2]−prefix[x1−1][y2]−prefix[x2][y1−1]+prefix[x1−1][y1−1]
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix[x2][y2] - prefix[x1-1][y2] - prefix[x2][y1-1] + prefix[x1-1][y1-1]
    print(result)