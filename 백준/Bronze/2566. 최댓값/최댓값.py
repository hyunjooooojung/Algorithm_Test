arr = [list(map(int, input().split())) for _ in range(9)]

max_number = 0
max_row, max_col = 0, 0
for i in range(9):
    for j in range(9):
        if max_number <= arr[i][j]:
            max_row = i+1
            max_col = j+1
            max_number = arr[i][j]

print(max_number)
print(max_row, max_col)