import sys
T = int(sys.stdin.readline())

for _ in range(T):
    stack = []
    string = sys.stdin.readline()
    
    for s in string:
        if s == "(":
            stack.append(s)
        elif s == ")":
            if stack:
                stack.pop()
            else:
                stack.append(s)
                break
    
    if stack:
        print("NO")
    else:
        print("YES")