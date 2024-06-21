#백준 24511번
#https://www.acmicpc.net/problem/24511
import sys
input = sys.stdin.readline
from collectios import deque
a = []
b_queue = []
b_stack = []
c = []

num = int(input())
a.append(list(map(int, input().split()))) #0이면 큐, 1이면 스택
b.append(list(map(int, input().split()))) #초기 상태(queuestack의)
leng = int(input())
c.append(list(map(int, input().split())))  #삽입할 원소의 배열
d = []


        


