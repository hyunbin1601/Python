#https://velog.io/@yyj8771/Python-heapq%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%B5%9C%EC%86%8C-%ED%9E%99-%EC%B5%9C%EB%8C%80-%ED%9E%99
#백준 11279번 문제 
#heapq 라이브러리는 기본적으로 최소힙

import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []

max_heap = []


for i in range(num):
    number = int(input())
    if number == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -number)
            
                