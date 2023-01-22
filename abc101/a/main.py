S = input()

answer = 0

for i in S:
    if i == "+":
        answer += 1
    elif i == "-":
        answer -= 1

print(answer)
