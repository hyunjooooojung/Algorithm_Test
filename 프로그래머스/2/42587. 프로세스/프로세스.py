from collections import deque

def solution(priorities, location):
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (우선순위, 인덱스) 저장
    answer = 0  # 실행 순서

    while queue:
        current = queue.popleft()  # 첫 번째 프로세스를 꺼냄

        # 현재 프로세스보다 높은 우선순위가 큐에 존재하는지 확인
        if any(current[0] < q[0] for q in queue):
            queue.append(current)  # 우선순위가 더 높다면 다시 큐에 삽입
        else:
            answer += 1  # 실행됨
            if current[1] == location:  # 우리가 찾던 프로세스라면 종료
                return answer
