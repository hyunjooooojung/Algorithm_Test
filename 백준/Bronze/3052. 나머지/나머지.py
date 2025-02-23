import sys
numbers = [int(sys.stdin.readline()) % 42 for i in range(1, 11)]
numbers = set(numbers)
print(len(numbers))