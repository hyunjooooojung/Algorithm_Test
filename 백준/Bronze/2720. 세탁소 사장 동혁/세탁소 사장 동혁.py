import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    C = int(input()) # 거스름돈(센트)
    change = C
    a, b, c, d = 0, 0, 0, 0 # 쿼터, 다임, 니켈, 페니
    while change:
        a += change // 25
        change -= (a*25)
        b += change // 10
        change -= (b*10)
        c += change // 5
        change -= (c*5)
        d += change // 1
        change -= (d*1)

        if change == 0:
            print(a, b, c, d)
            break