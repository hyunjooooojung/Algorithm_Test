import sys
input = sys.stdin.readline

# 이진탐색으로
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))
arr.sort()

for number in numbers:
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == number:
            print(1)
            break
        elif arr[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    else:
        print(0)

# # set으로 받아서
# N = int(input())
# arr = set(map(int, input().split()))
# M = int(input())
# numbers = list(map(int, input().split()))

# for number in numbers:
#     if number in arr:
#         print(1)
#     else:
#         print(0)
