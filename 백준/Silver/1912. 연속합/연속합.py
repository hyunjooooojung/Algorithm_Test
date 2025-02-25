n = int(input())
numbers = list(map(int, input().split()))

answer = [0] * (n+1) # 누적합을 담을 배열
for i in range(n):
    answer[i+1] = max(answer[i] + numbers[i], numbers[i])

answer.remove(answer[0]) # answer[1] 부터 할당되니까 answer[0] 삭제
print(max(answer))