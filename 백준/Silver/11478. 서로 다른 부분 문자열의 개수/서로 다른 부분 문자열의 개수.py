import sys
input = sys.stdin.readline

S = input().strip()

answer = set()
for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        answer.add(S[i:j])
print(len(answer))