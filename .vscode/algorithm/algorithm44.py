n = int(input()) #소인수분해하고자 하는 수
a = [] #오름차순으로 출력할 리스트
i = 2
while i<=n:  #i가 n보다 작거나 같을 때까지는 계속 반복
    
    if n == 1:
        break
    if n % i == 0:
        a.append(i)
        n = n / i
    
    else:
        i = i + 1
    
            
        
    
a.sort()

for i in range(len(a)):
    print(a[i])
        
            
    