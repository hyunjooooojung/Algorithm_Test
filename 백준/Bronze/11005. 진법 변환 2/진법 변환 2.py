import sys
input = sys.stdin.readline

def radix_change(num, radix):
    if num == 0:
        return '0'
    
    numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(numbers[digit])

    return ''.join(reversed(nums))

N, B = map(int, input().split()) # 10진법 수 N -> B진법으로 변환
print(radix_change(N, B))