a, b = map(int, input().split())

c = []
d = 1


for i in range(a):
    if a % d == 0:
        c.append(d)
        
    d = d + 1
    
        
if b > len(c):
    print(0)
else:
    print(c[b-1])
    