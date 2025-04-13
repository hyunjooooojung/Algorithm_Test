import sys
input = sys.stdin.readline

from collections import deque

N, K = map(int, input().split()) # 수빈 : N / 동생 : K
queue = deque([(N, 0)])
visited = [0] * 100001

while queue:
    now, time = queue.popleft()

    if now == K:
        print(time)
        break

    for i in (now-1, now+1, 2*now):
        if 0 <= i <= 100000 and visited[i] == 0:
            visited[i] = time + 1
            queue.append((i, time+1))