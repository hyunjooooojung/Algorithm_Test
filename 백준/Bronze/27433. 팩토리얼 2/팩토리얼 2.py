import sys
input = sys.stdin.readline

N = int(input())

def facto(n):
    if n < 2:
        return 1
    else:
        return n * facto(n-1)

print(facto(N))