def back(n):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(n, N+1):
        answer.append(i)
        back(i)
        answer.pop()

N, M = map(int, input().split())
answer = []
back(1)