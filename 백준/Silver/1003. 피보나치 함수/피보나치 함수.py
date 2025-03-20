import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    count0, count1 = 1, 0
    for i in range(N):
        count0, count1 = count1, count0+count1
    print(count0, count1)