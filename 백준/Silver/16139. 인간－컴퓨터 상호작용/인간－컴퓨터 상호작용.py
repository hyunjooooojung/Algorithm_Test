import sys
input = sys.stdin.readline

S = input() # 문자열
q = int(input()) # 질문의 수

for _ in range(q):
    a, l, r = input().split()

    count = 0
    for s in S[int(l):int(r)+1]:
        if a == s:
            count += 1
    
    print(count)