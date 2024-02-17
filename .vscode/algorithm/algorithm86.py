####소수 판별 함수(에라토스테네스의 체)####
# def is_prime_number(n):
#     # 2부터 n까지의 모든 수에 대하여 소수 판별
#     array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

#     # 에라토스테네스의 체
#     for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
#         if array[i] == True: # i가 소수인 경우(남은 수인 경우)
#             # i를 제외한 i의 모든 배수를 지우기
#             j = 2
#             while i * j <= n:
#                 array[i * j] = False
#                 j += 1

#     return [ i for i in range(2, n+1) if array[i] ]

# # N이 1,000,000 이내로 주어지는 경우 활용할 것 => 이론상 400만번 정도 연산이고 메모리도 충분함

# print(is_prime_number(26))

import math

a, b = map(int, input().split())


def is_prime_number(n):
    array = [True for i in range(n+1)] 
    for i in range(2, int(math.sqrt(n)) + 1): 
        if array[i] == True: 
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1
    return [ i for i in range(2, n+1) if array[i] ]

if a == 1:
    arr = is_prime_number(b)
    for i in range(len(arr)):
        print(arr[i])
else:
    arr1 = is_prime_number(a)
    arr2 = is_prime_number(b)

    
    for i in arr1:
        if i in arr2:
            arr2.remove(i)

    cnt = 0
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            cnt += 1
    if cnt == 0:
        arr2.append(a)
        arr2.sort()
        
        
    for i in range(len(arr2)):
        print(arr2[i])



