N = input()

sn = 0

for i in N:
    sn += int(i)

if (int(N) % sn) == 0:
    print("Yes")
else:
    print("No")
