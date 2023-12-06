#쿼터: 0.25달러 다임: 0.1 달러 니켈: 0.05 달러 페니: 0.01달러

cnt = int(input())
arr = []
num = [25, 10, 5, 1]

for i in range(cnt):
    arr.append(int(input()))

for i in range(len(arr)):  #배열의 크기만큼
    for j in num:   #배열에서 하나씩 가져오므로
        print(arr[i] // j, end = ' ')  #몫 출력
        arr[i] = arr[i] % j   #나머지, 마지막의 경우 나누는 대상이 1이므로 그대로 나온다
    print()
        
    
    
    