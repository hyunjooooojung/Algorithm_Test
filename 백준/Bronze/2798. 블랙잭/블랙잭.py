import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

max_sum = 0
for comb in combinations(numbers, 3):
    if sum(comb) <= M:
        max_sum = max(max_sum, sum(comb))

print(max_sum)