import sys
input = sys.stdin.readline

# permutations 라이브러리로 푸는법
# from itertools import permutations

# N, M = map(int, input().split())
# p = permutations(range(1, N+1), M)
# for i in p:
#     print(" ".join(map(str, i)))

# 백트래킹
N, M = map(int, input().split())
answer = []

def back():
    if len(answer) == M:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, N+1):
        if i not in answer:    
            answer.append(i)   
            back()             
            answer.pop()       
                               
back()