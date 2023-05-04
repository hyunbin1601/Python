import sys

n = int(sys.stdin.readline())  #n으로 입력값을 받는다

for i in range(n):
    for j in range(n-i-1):
        print(" ", end='')
    for k in range(2*i+1):
        print("*", end = '')
    print()

for i in range(n-1):
    for j in range(i+1):
        print(" ", end='')
    for k in range(2*(n-1)-(i*2+1)):  #끝 숫자는 포함이 되지 않는다
        print("*", end='')
    print()