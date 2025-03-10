import sys

string = sys.stdin.readline().rstrip()
for s in string:
    if s.isupper():
        print(s.lower(), end="")
    elif s.islower():
        print(s.upper(), end="")

# print(sys.stdin.readline().rstrip().swapcase())