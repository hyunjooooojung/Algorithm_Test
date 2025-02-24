import sys

N = int(sys.stdin.readline())

students = list(map(int, sys.stdin.readline().split()))
stack = [] # 대기 공간
start = 1 # 라인에 1번부터 순서대로 들어갈 수 있으니까 1부터 시작

for s in students:
    stack.append(s)

    while stack and stack[-1] == start:
        stack.pop()
        start += 1
    
if stack:
    print("Sad")
else:
    print("Nice")