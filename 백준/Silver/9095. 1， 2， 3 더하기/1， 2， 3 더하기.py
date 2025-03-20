import sys
input = sys.stdin.readline

T = int(input())

def number(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    if n > 3:
        return (number(n-3) + number(n-2) + number(n-1))

for _ in range(T):
    n = int(input())
    print(number(n))