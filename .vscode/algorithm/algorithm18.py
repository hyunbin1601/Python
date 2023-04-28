# #공백 단위로 수를 받아 리스트에 저장하는 함수
# #list(map(int, input().split())) -> split()메소드는 어떤 언급이
# #없으면 공백 단위로 수를 끊는다
# #시간초과 실화임? 빠른정렬
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# arr = list(map(int, input().split()))
# A.sort()  #분류해야 시간이 덜 걸린다

# for num in arr:
#     lt, rt = 0, N-1
#     isExist = False
    
#     while lt <= rt:
#         mid = (lt+rt)//2
#         if num == A[mid]:
#             isExist = True #비교하려는 값의 중간값부터 시작한다 있으면 true
#             print(1)
#             break  #while 반복문에서 탈출한다, for 반복문에서 탈출은 안됨
#         elif num > A[mid]:
#             lt = mid + 1
#         else:
#             rt = mid - 1
            
#     if isExist == False:    #not -> 아직도 False이냐를 물어봄
#         print(0)  #0출력       


# #이진 탐색을 이용한 알고리즘
# #계속해서 중간값을 찾아나가는 문제이다

def binary_serch(a, x, start, end): #함수 정의, 클래스는 안만듦
    if start > end:
        return 0
    
    m = (start + end) // 2 #2를 나눈 값의 정수 부분만 출력함
    if a[m] == x:
        return 1
    elif a[m] > x:
        return binary_serch(a, x, start, m-1)
    else:
        return binary_serch(a, x, m+1, end)  #이분탐색으로 백준 문제 풀기
    
#함수 생성

n = int(input()) #입력값은 기본적으로 문자열로 들어가므로, 정수형으로 형변환을 해 줘야함
a = list(map(int, input().split())) #split() -> 스페이스바 기준으로 입력값을 받고, map을 이용해 입력값을 함수를 거쳐 리스트에 저장토록 함
m = int(input())
m_l = list(map(int, input().split()))
a = sorted(a) #a를 정렬한 다음에 a 리스트에 다시 저장한다. 

for i in m_l:
    if binary_serch(a, i, 0, n-1):    #0이면 false, 1이면 true
        print(1)
    else:
        print(0)
        
#이진탐색 문제, 알고리즘의 시간 복잡도를 고려해서 풀자.
#이진탐색 문제 시간 알고리즘은 O(lgn)이라서 10만개의 경우의 수에도 조금 더 빠르게 처리할 수 있다