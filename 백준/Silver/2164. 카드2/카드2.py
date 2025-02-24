import sys
from collections import deque

N = int(sys.stdin.readline())
cards = deque(i for i in range(1, N+1)) # deque로 받음

while True:
    if len(cards) == 1: # 카드 한장 남을 때까지
        break

    # 제일 위에있는 카드 버림
    cards.popleft()

    # 제일 위에있는 카드를 맨 아래로 옮김
    cards.append(cards[0])
    cards.popleft()

print(*cards)