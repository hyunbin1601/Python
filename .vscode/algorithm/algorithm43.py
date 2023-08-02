# import sys

# m = int(sys.stdin.readline())
# n = int(sys.stdin.readline())

# #첫째줄에는 합, 둘째줄에는 소수 중 최솟값 입력
# a = 0
# b = 0
# c = []
# d = []
# e = []
# for i in range(m, n+1):
#     c.append(i)  #m과 n 사이의 숫자 저장
    
# for i in range(n-m+1):
#     k = 0
#     for j in range(c[i]):
#         if c[i] == 1:
#             break
#         elif c[i] % (j+1) == 0:
#             k = k + 1
#     d.append(k)
    
# for i in range(n-m+1):
#     if d[i] <=2 and d[i] > 0:
#         a = a + c[i]
#         e.append(c[i])

# if len(e) >= 1:
#     b = e[0]
#     for i in range(len(e)-1):
#         if b > e[i+1]:
#             b = e[i+1]
        
#     print(a)
#     print(b)
    
# else:
#     print(-1)

#너무 복잡하게 풀었다...ㅠㅠ
m = int(input())
n = int(input())

a=[]

for i in range(m, n+1):
    p = 0 
    
    if i != 1:
        for j in range(2, i):  
            if i % j == 0:
                p = p + 1
                break  #안걸면 시간초과가 날 수 있음
         
        if p == 0:
            a.append(i)
                         
    
   
        
if len(a) > 0:
    print(sum(a))
    print(min(a))
    
else:
    print(-1)
            