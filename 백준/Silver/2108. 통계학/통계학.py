import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

print(round(sum(numbers) / N)) # 산술평균
print(numbers[(len(numbers) // 2)]) # 중앙값

# 최빈값
count_dict = dict()
for n in numbers:
    if n in count_dict:
        count_dict[n] += 1
    else:
        count_dict[n] = 1

max_count = [] # 최빈값 여러개인 경우 처리
for m in count_dict:
    if count_dict[m] == max(count_dict.values()):
        max_count.append(m)
if len(max_count) == 1:
    print(max_count[0])
else:
    print(max_count[1])

print(max(numbers) - min(numbers)) # 범위