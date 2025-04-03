import heapq

def solution(scoville, K):
    heapq.heapify(scoville) # 리스트를 최소힙으로 변환
    count = 0
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)
        count += 1
    
    if scoville[0] < K:
        return -1
    
    return count