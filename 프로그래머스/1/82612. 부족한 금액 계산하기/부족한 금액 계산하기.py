def solution(price, money, count):
    for i in range(1, count+1):
        money -= price * i
    
    if money >= 0: # 금액이 부족하지 않으면
        return 0
    else:
        return abs(money)
