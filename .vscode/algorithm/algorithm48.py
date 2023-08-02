n = int(input()) #n번째 영화의 제목에 들어간 수 출력
result = []

num = 666  #전역변수

while True:  
    if str(num).count("666") >= 1:
        #count 파이썬 함수는 문자열 합을 세는 함수이다
        result.append(num)
        
    num = num + 1
    if len(result) > n:   #숫자 666부터 계속 반복(브루트 포스)
        break  #반복문 탈출
    
print(result[n-1])    
        
    
    
    
    
    