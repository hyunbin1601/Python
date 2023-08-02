num = int(input()) #입력값을 받는다

p = []
c = 0
a = list(map(int, input().split())) #a라는 리스트를 만듦
    
for i in range(num):
    k = 0
    for j in range(a[i]):
        if a[i] == 1:
            break
        
        elif a[i] % (j+1) == 0:
            k = k + 1
            
    p.append(k)
    
for i in range(num):
    if p[i] <= 2 and p[i] > 0 :
        c = c + 1
print(c)