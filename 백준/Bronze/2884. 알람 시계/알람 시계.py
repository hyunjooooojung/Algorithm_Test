H, M = map(int, input().split())

if M >= 45:
    print(H, M-45)
elif M < 45 and H == 0:
    H = 23
    M += 60
    print(H, M-45)
elif M < 45:
    H -= 1
    M += 60
    print(H, M-45)