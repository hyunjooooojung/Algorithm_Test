import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers_dict = {}
name_dict = {}

for i in range(1, N+1):
    name = input().strip()

    numbers_dict[i] = name
    name_dict[name] = i

for _ in range(M):
    target = input().strip()

    if target.isdigit():
        print(numbers_dict[int(target)])
    else:
        print(name_dict[target])