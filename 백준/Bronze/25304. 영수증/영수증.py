X = int(input()) # 총 금액 
N = int(input()) # 물건 종류 개수

total = 0
for i in range(N):
    a, b = map(int, input().split())
    total += (a*b)

if total == X:
    print("Yes")
else:
    print("No")