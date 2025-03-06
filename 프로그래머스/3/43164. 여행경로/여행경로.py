from collections import defaultdict

def solution(tickets):
    
    # 그래프 생성 (항공권 정보 저장) - 가능한 경로가 2개 이상인 경우도 하나의 키에 같이 저장하기 위해서!
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    
    # 알파벳 순서가 앞서는 경로를 위해 정렬 (reverse 후 pop 사용)
    for key in graph:
        graph[key].sort(reverse=True)
    
    answer = []
    def dfs(airport):
        while graph[airport]: # 현재 공항에서 출발할 항공권이 남아있는 동안
            next_airport = graph[airport].pop()  # 사전순으로 가장 빠른 공항 선택
            dfs(next_airport) # 다음 공항
        answer.append(airport) # 경로 추가 (DFS 종료 후 추가)

    dfs("ICN") # 항상 "ICN"에서 출발
    
    return answer[::-1] # DFS 종료 후 역순으로 반환