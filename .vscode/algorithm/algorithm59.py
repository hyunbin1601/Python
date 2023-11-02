#가능한 진법의 범위: 36진법

num1, num2 = map(int, input().split())

arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def converSolution(n, m):
    rev_base = ''   #결과값을 저장할 문자열
    
    while n > 0:    #n은 10진수
        mod = arr[n%m]   #나머지 값
        rev_base += str(mod)  #string 형변환
        n = n // m    #n을 m으로 나눌 때, 그 몫
        
    return rev_base[::-1]   #반대로 정렬

print(converSolution(num1, num2))
    