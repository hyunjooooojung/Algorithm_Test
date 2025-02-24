import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())

yosepus = deque(i for i in range(1, N+1)) # deque(range(1, N+1))
answer = []

while yosepus:
    yosepus.rotate(-(K-1)) # K번째 사람이 맨 앞으로 오도록 회전
    answer.append(yosepus.popleft()) # 맨 앞의 K번째 사람 제거

print(f"<{', '.join(map(str, answer))}>")

# # 내가 작성한 코드 : IndexError
# '''
# 1. K-1 인덱스를 직접 참조하는 문제

# yosepus[K-1]을 사용해서 K번째 원소를 찾고 삭제하는데, 원의 크기가 줄어들면서 K-1이 올바른 위치를 가리키지 않을 수 있음.
# 특히, K가 리스트 크기보다 크거나, 리스트가 줄어들면서 K-1이 범위를 벗어나면 IndexError가 발생할 가능성이 있음.

# 2. 잘못된 로테이션 (rotate(-2))

# rotate(-2)는 리스트의 길이에 관계없이 항상 2칸을 회전시키므로, K번째 요소를 찾는 올바른 방식이 아님.
# 요세푸스 문제는 매번 남은 사람들 중에서 K번째 사람을 제거하는 과정이 반복되어야 하는데, rotate(-2)는 고정된 움직임이기 때문에 잘못된 위치에서 요소를 제거할 가능성이 큼.

# 3. 종료 조건 확인 (len(yosepus) <= 2)

# len(yosepus) <= 2인 경우, 단순히 앞에서부터 제거하는데, 원래 요세푸스 문제는 마지막까지 K번째 규칙을 유지해야 함.
# 예를 들어, len(yosepus) == 2일 때도 K번째를 찾아야 하지만, 이 코드에서는 그냥 popleft()를 하므로 결과가 다를 수 있음.
# '''
# import sys
# from collections import deque

# N, K = map(int, sys.stdin.readline().split())

# yosepus = deque(i for i in range(1, N+1))

# answer = []
# while True:
#     if len(yosepus) == 0:
#         break

#     if len(yosepus) > 2:
#         answer.append(yosepus[K-1])
#         yosepus.remove(yosepus[K-1])
#         yosepus.rotate(-2)
#     elif len(yosepus) <= 2:
#         answer.append(yosepus[0])
#         yosepus.popleft()

# print(f"<{', '.join(map(str, answer))}>")