N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i, j+1):
        basket[n-1] = k

print(*basket)