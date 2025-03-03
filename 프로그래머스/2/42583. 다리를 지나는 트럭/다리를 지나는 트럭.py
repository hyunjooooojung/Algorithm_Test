from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()  # 현재 다리를 건너는 트럭 (무게, 경과 시간)
    truck_weights = deque(truck_weights) # 대기 트럭을 큐로 변환
    
    time = 0 # 소요시간
    total_weight = 0 # 다리 위의 총 트럭 무게
    
    while truck_weights or bridge:
        time += 1 
        # 1. 다리에서 이동 시간이 다 된 트럭 제거
        if bridge and bridge[0][1] == bridge_length:
            truck_out = bridge.popleft()
            total_weight -= truck_out[0]  # 다리에서 나간 트럭 무게 제거
        
        # 2. 새로운 트럭을 다리에 올릴 수 있는지 확인
        if truck_weights and (total_weight + truck_weights[0] <= weight):
            truck_in = truck_weights.popleft()
            bridge.append((truck_in, 0)) # 새로운 트럭 추가
            total_weight += truck_in # 다리 위 무게 업데이트
            
        # 3. 다리 위에 있는 모든 트럭의 경과 시간 +1
        bridge = deque((w, t+1) for w, t in bridge)

    return time