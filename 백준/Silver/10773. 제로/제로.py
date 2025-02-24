import sys
K = int(sys.stdin.readline())

stack = []
for _ in range(K):
    x = int(sys.stdin.readline())
    if x == 0:
        stack.pop()
    else:
        stack.append(x)

print(sum(stack))