import sys

N = int(input())

stack = []
for _ in range(N):
    a = list(map(int, sys.stdin.readline().split()))
    
    # 1 X 명령
    if a[0] == 1:
        stack.append(a[1])
    # 2 명령
    elif a[0] == 2:
        print(stack.pop() if stack else -1)
    # 3 명령
    elif a[0] == 3:
        print(len(stack))
    # 4 명령
    elif a[0] == 4:
        print(1 if len(stack) == 0 else 0)
    # 5 명령
    elif a[0] == 5:
        print(stack[-1] if stack else -1)