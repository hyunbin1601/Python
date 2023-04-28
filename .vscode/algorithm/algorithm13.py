#재귀함수를 이용한 팩토리얼 해결 문제
#0을 입력할 경우, 1이 출력된다

def recursivealgorithm(num):
    if num ==0:
        return 1
    else:
        return recursivealgorithm(num-1) *num
    
    
a = recursivealgorithm(int(input()))
print(a)
    
    


# for:
#     for:
#         for:
            
#재귀 알고리즘은 위와 같이 for문을 계속 거슬러 올라가면서 실행된다            
            