#팩토리얼 문제
import sys
input = sys.stdin.readline

num = int(input())
cnt = 1

for i in range(1, num):
    cnt = cnt * (i+1)
    
print(cnt)