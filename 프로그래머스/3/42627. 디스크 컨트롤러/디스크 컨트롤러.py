import heapq

def solution(jobs):
    jobs.sort() # 요청 시간 순으로 정렬
    heap = []
    
    time = 0 # 현재시간
    total = 0 # 대기시간
    i = 0 # jobs 인덱스
    count = 0 # 처리된 작업 수
    
    while count < len(jobs):
        # 현재 시점까지 요청된 작업을 힙에 추가
        while i < len(jobs) and jobs[i][0] <= time:
            heapq.heappush(heap, (jobs[i][1], jobs[i][0])) # (작업시간, 요청시간)
            i += 1
        
        if heap:
            dur, req = heapq.heappop(heap)
            time += dur
            total += (time - req)
            count += 1
        else:
            time += 1
    return total // len(jobs)