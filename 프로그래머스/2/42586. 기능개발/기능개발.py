from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    for i in range(len(progresses)):
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    while queue:
        count = 1 # 첫번째 배포날에 배포하는 개수
        first = queue.popleft() # 맨 처음 원소
        
        while queue and first >= queue[0]:
            count += 1
            queue.popleft()
        
        answer.append(count)
        
    return answer