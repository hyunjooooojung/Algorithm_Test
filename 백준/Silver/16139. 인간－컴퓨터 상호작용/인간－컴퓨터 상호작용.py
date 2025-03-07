# https://developer-project.tistory.com/418 님의 풀이를 참고함.

import sys
input = sys.stdin.readline

S = input().rstrip() # 문자열
q = int(input()) # 질문의 수

count = [[0] * 26]
for i in range(len(S)):
    count.append(count[len(count) - 1][:])
    count[i+1][ord(S[i]) - 97] += 1

for _ in range(q):
    a, l, r = input().split()
    result = count[int(r) + 1][ord(a) - 97] - count[int(l)][ord(a) - 97]
    print(result)