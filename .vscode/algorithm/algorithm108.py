#https://www.acmicpc.net/problem/1010

# import sys
# input = sys.stdin.readline
# import math

# num = int(input())

# for _ in range(num):
#     a, b = map(int, input().split())
#     a_fac = math.factorial(a)
#     b_fac = math.factorial(b)
#     k_fac = math.factorial(b-a)
#     print(int(b_fac / a_fac / k_fac))

import sys
input = sys.stdin.readline
import math

num = int(input())

for _ in range(num):
    a, b = map(int, input().split())
    print(int(math.comb(b, a)))