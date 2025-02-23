A, B = map(str, input().split())
print(max(int(A[::-1]), int(B[::-1])))

# int(A[::-1]) == int("".join(reversed(str(A))))