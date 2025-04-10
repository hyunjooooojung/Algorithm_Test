import sys
input = sys.stdin.readline

N, M = map(int, input().split())

strings = set()
for _ in range(N):
    strings.add(input().strip())

count = 0
for _ in range(M):
    target_string = input().strip()
    if target_string in strings:
        count += 1
print(count)