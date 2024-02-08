# num = int(input())
# arr1 = []
# arr2 = []

# for i in range(num):
#     a, b = map(int, input().split())
#     arr1.append(a)
#     arr2.append(b)
    
# arr1.sort()
# arr2.sort()

# for i in range(num):
#     print(arr1[i], end=' ')
#     print(arr2[i])
        
num = int(input())

arr1 = []

for i in range(num):
    arr2 = list(map(int, input().split()))
    arr1.append(arr2)
    
arr1.sort()

for i in range(num):
    print(*arr1[i])
    
            