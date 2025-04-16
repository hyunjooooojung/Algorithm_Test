import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    commands = input().split()

    if commands[0] == 'add':
        S.add(int(commands[1]))
    elif commands[0] == 'remove':
        S.discard(int(commands[1]))
    elif commands[0] == 'check':
        if int(commands[1]) in S:
            print(1)
        else:
            print(0)
    elif commands[0] == 'toggle':
        if int(commands[1]) in S:
            S.discard(int(commands[1]))
        else:
            S.add(int(commands[1]))
    elif commands[0] == 'all':
        S = set([i for i in range(1, 21)])
    elif commands[0] == 'empty':
        S = set()