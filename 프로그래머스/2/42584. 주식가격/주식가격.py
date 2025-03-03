from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    
    while prices:
        time = 0
        now = prices.popleft()
        for p in prices:
            time += 1
            if p < now:
                break
        answer.append(time)
    
    return answer