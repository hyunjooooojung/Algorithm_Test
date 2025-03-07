import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N: 전체 날짜 수, K: 연속날짜 수
numbers = list(map(int, input().split()))

prefix = [sum(numbers[:K])] # 처음 K번째까지의 누적합으로 초기화

for i in range(N-K):
    prefix.append(prefix[i] - numbers[i] + numbers[K+i])    

print(max(prefix))