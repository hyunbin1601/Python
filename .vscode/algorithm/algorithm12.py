a = []
for i in range(5):   #인덱스로는 0부터 4번까지인걸로, 5번 반복한다는 의미
    a.append(int(input()))

avg = 0
sum = 0
middle = 0 
tmp = 0

for i in range(5):
    sum = sum + a[i]
    avg = sum//5   
    
print(avg)
for j in range(4): #0부터 len(a)-2번까지
    for k in range(j+1, 5):
        if a[j] >= a[k]:
            tmp = a[k]
            a[k] = a[j]
            a[j] = tmp

middle = a[2]
print(a)
    