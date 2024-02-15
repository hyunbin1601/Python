a, b = map(int, input().split())
arr1 = []
arr2 = []
cnt = 0

for i in range(a):
    arr1.append(input())
    
for i in range(b):
    arr2.append(input())
    
for i in arr2:
    for j in arr1:
        if i == j:
            cnt += 1

print(cnt)