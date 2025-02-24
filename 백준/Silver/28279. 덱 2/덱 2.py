import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque()
for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))
    if command[0] == 1:
        dq.appendleft(command[1])
    elif command[0] == 2:
        dq.append(command[1])
    elif command[0] == 3:
        print(dq.popleft() if dq else -1)
    elif command[0] == 4:
        print(dq.pop() if dq else -1)
    elif command[0] == 5:
        print(len(dq))
    elif command[0] == 6:
        print(1 if len(dq) == 0 else 0)
    elif command[0] == 7:
        print(dq[0] if dq else -1)
    elif command[0] == 8:
        print(dq[-1] if dq else -1)