import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    score, sum_score = 0, 0
    result = list(input())
    for r in result:
        if r == "O":
            score += 1
            sum_score += score
        elif r == "X":
            score = 0
    print(sum_score)