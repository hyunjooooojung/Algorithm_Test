import sys
input = sys.stdin.readline

def self_number(n):
    number = n + sum(map(int, str(n)))
    return number

result = set()
for i in range(10000):
    result.add(self_number(i))
for i in range(1, 10001):
    if i not in result:
        print(i)