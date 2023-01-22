K = int(input())

tmp = []
for i in range(1, 100):
    S = str(i)
    sn = 0
    for s in S:
        sn += int(s)

    tmp.append(sn / i)

print(tmp)
