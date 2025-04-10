import sys
input = sys.stdin.readline

N = int(input())
numbers = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
    if target in numbers:
        print(1, end=" ")
    else:
        print(0, end=" ")