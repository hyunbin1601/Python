#세 정수 받기
'''a, b, v = map(int, input().split())
here = 0
cnt = 1

while here <= v:  #here의 값이 같거나 작을 때까진 계속 반복
    here += a
    if here >= v:
        break
    else:
        here -= b
        cnt += 1
print(cnt)'''
import sys
import math

a, b, v = map(int, sys.stdin.readline().split())
cnt = 0
#while문 안쓰고 푸는 방법
cnt = (v-b) / (a-b)
print(math.ceil(cnt))