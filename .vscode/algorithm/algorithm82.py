import math

num = int(input())
arr = []

for i in range(num):
    a, b = map(int, input().split())
    arr.append(math.lcm(a, b))
    
for i in range(len(arr)):
    print(arr[i])
    
