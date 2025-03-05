def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    for i in range(len(A)):
        answer += A[i] * B[i]

    return answer
    
    # 한줄로 끝내는 코드네... -> zip 함수 사용
    # return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])