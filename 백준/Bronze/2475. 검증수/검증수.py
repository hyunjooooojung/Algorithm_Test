import sys
input = sys.stdin.readline
numbers = map(int, input().split())

sum_number = 0
for n in numbers:
    sum_number += n**2

print(sum_number % 10)