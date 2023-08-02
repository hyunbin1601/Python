import sys

num = list(map(int, sys.stdin.readline().split()))


for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (num[0] * i + num[1] * j == num[2]) and (num[3] * i + num[4] * j == num[5]):
            print(i, end = ' ')
            print(j)
            break
        
    