import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

count_dict = {}
for number in numbers:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

for target in targets:
    if target in count_dict:
        print(count_dict[target], end=" ")
    else:
        print(0, end=" ")