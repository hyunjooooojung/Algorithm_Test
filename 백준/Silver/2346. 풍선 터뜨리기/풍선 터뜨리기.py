import sys
from collections import deque

N = int(sys.stdin.readline())
balloons = deque(enumerate(map(int, sys.stdin.readline().split())))

answer = []
while balloons:
    idx, number =  balloons.popleft()
    answer.append(idx + 1)

    if number > 0:
        balloons.rotate(-(number-1))
    elif number < 0:
        balloons.rotate(-number)

print(' '.join(map(str, answer)))