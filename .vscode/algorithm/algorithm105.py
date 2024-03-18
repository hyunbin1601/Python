#파이썬의deque 라이브러리를 사용해서 푸는 문제
#큐와 리스트의 요소 2개를 모두 가지고 있음
#list() 함수로 리스트화해서 일반 리스트처럼 사용 가능
#popleft, appendleft로 큐처럼 왼쪽 끝의 요소 수정 가능, pop, append로 일반 리스트처럼 사용가능

import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
deq = deque()

for i in range(num):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        deq.appendleft(arr[1])
    elif arr[0] == 2:
        deq.append(arr[1])
    elif arr[0] == 3:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif arr[0] == 4:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif arr[0] == 5:
        print(len(deq))
    elif arr[0] == 6:
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 7:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    else:
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
        
        
