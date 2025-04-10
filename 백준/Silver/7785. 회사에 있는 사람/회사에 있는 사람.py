n = int(input())
datas = set()
for _ in range(n):
    record = input().split()
    if record[0] in datas:
        datas.remove(record[0])
    else:
        datas.add(record[0])

datas = sorted(list(datas), reverse=True)
for data in datas:
    print(data)