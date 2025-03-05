def solution(s):
    answer = ''
    s = s.strip().split(" ")
    numbers = [int(i) for i in s]
    
    return f"{str(min(numbers))} {str(max(numbers))}"