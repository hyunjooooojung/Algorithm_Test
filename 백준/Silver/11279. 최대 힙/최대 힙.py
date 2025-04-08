import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []

for _ in range(N):
    x = int(input())

    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(arr))
    else:
        heapq.heappush(arr, -x)