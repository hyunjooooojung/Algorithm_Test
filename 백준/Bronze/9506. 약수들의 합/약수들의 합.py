import sys
input = sys.stdin.readline

while True:
    n = int(input())

    if n == -1:
        break

    numbers = []
    for i in range(1, n):
        if n % i == 0:
            numbers.append(i)
    
    if sum(numbers) == n:
        print(f"{n} = {' + '.join(map(str, numbers))}")
    else:
        print(f"{n} is NOT perfect.")