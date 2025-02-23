word = input()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

time = 0
for w in word:
    for idx, di in enumerate(dial):
        if w in di:
            time += (idx + 3)

print(time)