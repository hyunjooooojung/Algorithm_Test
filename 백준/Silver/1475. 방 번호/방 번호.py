import sys
input = sys.stdin.readline

N = input().strip()
counts = [0] * 10

for i in N:
    counts[int(i)] += 1

counts[6] = counts[9] = (counts[6] + counts[9] + 1) // 2
print(max(counts))