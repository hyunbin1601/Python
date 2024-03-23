#deque이용해서 푸는문제
import sys
from collections import deque
input = sys.stdin.readline

num = int(input())

lst = deque(enumerate(map(int, input().split())))  #deque 선언
ans = []


for _ in range(num):
    idx, a = lst.popleft()
    ans.append(idx+1)
    if num >= abs(a):
        if a>0:
            lst.rotate(-(a-1))   #양수값이 들어오면 왼쪽 방향으로 회전, 음수값이 들어오면 오른쪽 방향으로 회전
        else:
            lst.rotate(-a)    
for i in range(num):
    print(ans[i], end=' ')
    



        