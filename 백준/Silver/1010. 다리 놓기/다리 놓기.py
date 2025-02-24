import sys
from math import factorial

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    
    # M개 중에 N개를 고르는 경우의 수
    print((factorial(M)) // ((factorial(M-N)) * (factorial(N))))