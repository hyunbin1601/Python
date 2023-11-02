# 3번 - (2+1+2+4)^2 4번 - (2+1+2+4+8)^2

num = int(input())
numAdd = 2
numAdd2 = 0

for i in range(num):
    numAdd2 = numAdd2 + (2 ** i)
    
numAdd = numAdd + numAdd2
    
print(numAdd ** 2)