def back(n):
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    
    for i in range(n, N+1):
        if i not in answer:
            answer.append(i)
            back(i+1)
            answer.pop()

N, M = map(int, input().split())
answer = []
back(1)