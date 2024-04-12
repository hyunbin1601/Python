import sys
input = sys.stdin.readline

num = int(input())


p = -1
for i in range(int(num / 5), 0, -1):
    if num % 5 == 0:
        p = int(num / 5)
    else:
        r = num - (i * 5)
        if r % 3 == 0:
            p = i + int(r/3)
            break   #가장 처음으로 해당되는게 나오면 거기서 멈춰야함
if p == -1:
    d, r = divmod(num, 3)
    if r == 0:
        print(d)
    else:
        print(p)
else:
    print(p)


        