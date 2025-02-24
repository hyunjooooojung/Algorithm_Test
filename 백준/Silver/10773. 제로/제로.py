K = int(input())

stack = []
for _ in range(K):
    x = int(input())
    if x == 0:
        stack.pop(-1)
    else:
        stack.append(x)

print(sum(stack))