def solution(s):
    answer = ''
    s = s.strip().split(" ")
    numbers = [int(i) for i in s]
    
    answer += (str(min(numbers)))
    answer += " "
    answer += (str(max(numbers)))
    
    return answer