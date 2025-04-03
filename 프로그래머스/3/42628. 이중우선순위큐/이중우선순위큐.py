import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)  # 각 연산이 유효한지 표시
    
    for i, op in enumerate(operations):
        if op[0] == 'I':
            num = int(op[2:])
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        elif op == 'D 1':  # 최댓값 삭제
            while max_heap and visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                visited[max_heap[0][1]] = True
                heapq.heappop(max_heap)
        elif op == 'D -1':  # 최솟값 삭제
            while min_heap and visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = True
                heapq.heappop(min_heap)

    # 마지막으로 유효하지 않은 값 제거
    while min_heap and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]
