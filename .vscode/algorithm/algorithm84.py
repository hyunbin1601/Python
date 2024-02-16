import math

num = int(input())
arr=[]
cal=[]

for i in range(num):
    arr.append(int(input()))
    
for i in range(len(arr)-1):
    cal.append(arr[i+1]-arr[i])
    
idx = math.gcd(*cal)

idx2 = int(((arr[num-1] - arr[0]) / idx) + 1)
print(idx2 - num)
    