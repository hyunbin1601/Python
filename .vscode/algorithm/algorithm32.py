import sys

def fib1(n):
    
    if n == 1 or n ==2:
        
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
    
def fib2(n):
    global cnt
    f = [0 for i in range(n)]  #0부터 n까지 1차원 배열을 만듦
    
    f[0], f[1] = 1, 1   #각각 1을 넣어줘야함
    if n < 2:
        cnt = cnt + 1
       
    
    for i in range(2, n):
        cnt = cnt + 1
        f[i] = f[i-1] + f[i-2]   #배열에 값을 저장함
        
    return cnt

n = int(sys.stdin.readline())
cnt = 0
print(fib1(n), fib2(n))


    
    
def fibonacci(n):
    global count2
    f = [1] * (n + 1)
    for i in range(3, n + 1):
        count2 += 1
        f[i] = f[i-1] + f[i-2]
    return f[n]

N = int(input())
count2 = 0

print(fibonacci(N), count2)