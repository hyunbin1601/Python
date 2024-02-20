a, b = map(int, input().split())
arr1 = []  #집합 s
arr2 = []
cnt = 0

for i in range(a):
    arr1.append(input())
    
for i in range(b):
    arr2.append(input())
    
arr1.sort()
arr2.sort()
arr1_set = set(arr1)
arr2_set = set(arr2)    
for i in arr1_set:
    if i in arr2_set:
        cnt = cnt + 1 + (arr2.count(i)-1)
print(cnt)
