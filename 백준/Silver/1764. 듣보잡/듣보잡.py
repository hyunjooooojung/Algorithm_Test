import sys
input = sys.stdin.readline

N, M = map(int, input().split())

duddo_dict = set(input().strip() for _ in range(N))
bodo_dict = set(input().strip() for _ in range(M))

intersections = sorted(list(duddo_dict & bodo_dict))
print(len(intersections))
for i in intersections:
    print(i)