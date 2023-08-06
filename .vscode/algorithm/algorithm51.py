import sys
n = int(sys.stdin.readline())  #입력할 수의 개수

a = []

for i in range(n):
    a.append(int(sys.stdin.readline()))  #n번 입력받는다
    
a.sort()

for i in range(n):
    print(a[i])