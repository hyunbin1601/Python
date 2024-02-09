num = int(input())
arr = []

for i in range(num):
    xy = list(map(int, input().split()))
    arr.append(xy)
    
arr.sort()
arr.sort(key=lambda x:x[1])

# tmp = []

# for i in range(num):
#     for j in range(i):
#         if arr[i][1] > arr[j+1][1]:
#             tmp.append(arr[i])
#             arr[i] = arr[j+1]
#             arr[j+1] = tmp


            
for i in range(num):
    print(*arr[i])