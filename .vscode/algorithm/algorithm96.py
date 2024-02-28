#딕셔너리 자료형 이용

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = {}

for i in range(1, n+1):
    poke = input().rstrip()
    arr[i] = poke
    arr[poke] = i
    
    
for i in range(m):
    poke2 = input().rstrip()
    if poke2.isdigit():
        print(arr[int(poke2)])
    else:
        print(arr[poke2])