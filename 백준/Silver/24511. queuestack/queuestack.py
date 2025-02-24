import sys
from collections import deque

N = int(sys.stdin.readline()) # 자료구조 개수
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline()) # 삽입할 수열의 길이
C = list(map(int, sys.stdin.readline().split())) # queuestack에 삽입할 원소를 담고 있는 수열

queuestack = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 모으기
        queuestack.append(B[i])

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(M):
    queuestack.appendleft(C[i])
    print(queuestack.pop(), end= " ")