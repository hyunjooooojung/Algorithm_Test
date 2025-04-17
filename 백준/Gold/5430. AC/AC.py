import sys
input = sys.stdin.readline

from collections import deque

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    arr_str = input().strip()

    if n == 0:
        queue = deque()
    else:
        queue = deque(list(map(int, arr_str[1:-1].split(","))))

    reverse, error = False, False

    for command in p:
        if command == "R":
            reverse = not reverse
        elif command == "D":
            if len(queue) == 0:
                print("error")
                error = True
                break
            if reverse:
                queue.pop()
            else:
                queue.popleft()

    if not error:
        if reverse:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")