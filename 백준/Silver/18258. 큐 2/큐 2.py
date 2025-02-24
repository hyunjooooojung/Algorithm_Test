import sys
from collections import deque
# 시간제한 -> deque로 구현
N = int(sys.stdin.readline())

answer = deque()
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        answer.append(command[1])
    elif command[0] == "pop":
        print(answer.popleft() if answer else -1)
    elif command[0] == "size":
        print(len(answer))
    elif command[0] == "empty":
        print(1 if len(answer) == 0 else 0)
    elif command[0] == "front":
        print(answer[0] if answer else -1)
    elif command[0] == "back":
        print(answer[-1] if answer else -1)