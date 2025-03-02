N = int(input()) # 색종이 수

arr = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(N):
    A, B = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[A+i][B+j] = 1

count = 0
for a in arr:
    count += a.count(1)
print(count)