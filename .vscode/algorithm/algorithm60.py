#쿼터: 0.25달러 다임: 0.1 달러 니켈: 0.05 달러 페니: 0.01달러

cnt = int(input())
arr = []
num = [25, 10, 5, 1]

for i in range(cnt):
    arr.append(int(input()))

for i in range(len(arr)):
    for j in num:
        print(arr[i] // j, end = ' ')
        arr[i] = arr[i] % j   #나머지
    print()
        
    
    
    