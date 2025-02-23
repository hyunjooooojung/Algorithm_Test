import string

S = input()

lowers = list(string.ascii_lowercase)
for lower in lowers:
    if lower in S:
        print(S.index(lower), end=" ")
    else:
        print(-1, end=" ")