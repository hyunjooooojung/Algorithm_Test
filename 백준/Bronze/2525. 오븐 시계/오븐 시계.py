A, B = map(int, input().split()) # 현재 시각
C = int(input()) # 요리하는데 필요한 시간(분)

A = (((A * 60) + B + C) // 60) % 24
B = (B + C) % 60
print(A, B)