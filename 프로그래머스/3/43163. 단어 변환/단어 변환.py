from collections import deque

def check_word(word, check_word):
    # 한 글자만 다른 단어인지 확인
    count = 0
    for i in range(len(word)):
        if word[i] != check_word[i]:
            count += 1
    
    if count == 1:
        return True
    else:
        return False
    
def solution(begin, target, words): # BFS : 최소 단계 구하기
    
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    visited = set() # 방문한 단어 체크
    while queue:
        now_word, count = queue.popleft()
        
        if now_word == target:
            return count
        
        for word in words:
            if word not in visited and check_word(now_word, word):
                visited.add(word)  # 방문 체크
                queue.append((word, count+1))
                
    return answer