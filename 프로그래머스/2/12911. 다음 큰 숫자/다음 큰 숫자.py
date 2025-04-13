def solution(n):
    answer = 0
    binary_count = bin(n)[2:].count("1")
    
    for i in range(n, 1000001):
        if i > n and bin(i)[2:].count("1") == binary_count:
            answer = i
            break
    return answer