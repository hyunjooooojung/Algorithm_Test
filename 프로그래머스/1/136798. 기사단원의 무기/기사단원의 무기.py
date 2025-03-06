def check_number(number):
    count = 0
    for i in range(1, int(number**0.5)+1):
        if number % i == 0:
            count += 1
            if i ** 2 != number:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        if check_number(i) > limit:
            answer += power
        else:
            answer += check_number(i)
    return answer