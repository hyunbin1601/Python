import sys
input = sys.stdin.readline


num = int(input())

name = ["ChongChong"]

for _ in range(num):
    x, y = map(str, input().split())
    if x in name:
        name.append(y)
    elif y in name:
        name.append(x)
    else:
        continue
result = set(name)
print(len(result))
    