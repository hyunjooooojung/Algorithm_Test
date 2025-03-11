import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)

n = int(input())
print(f(n))