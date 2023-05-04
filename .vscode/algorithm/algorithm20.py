# card = int(input()) #상근이가 가지고 있는 카드의 개수
# number = list(map(int, input().split())) #공백 단위로 끊어서 리스트로 받는다

# search1 = int(input())
# search2 = list(map(int, input().split()))
# number.sort()
# search2.sort()

# def binarysearch(a, x, start, end):  #a는 탐색 대상 리스트, x는 찾고자 하는 값, start와 end는 탐색 당하는 리스트의 처음과 끝
#     if start > end:
#         return 0
#     mid = (start+end)//2  #중간에 위치한 인덱스에 있는 값을 의미
#     if a[mid] == x:     #찾을려는 값이 바로 존재할때
#         return a[start:end+1].count(x)    #start에서 end까지 모두 살펴본다는 의미
#     elif a[mid] > x:  #mid의 값이 x보다 클 경우
#         return binarysearch(a, x, start, mid-1)
#     elif a[mid] < x:
#         return binarysearch(a, x, mid+1, end)

# cnt = []
# for i in search2:
#     start = 0
#     end = len(number)-1  #card의 원소의 개수에서 1개를 뺌
#     cnt.append(binarysearch(number, i, start, end))
    
# print(cnt)
    
##### 시간초과 실화냐 #####    

import sys
from collections import Counter

M = int(sys.stdin.readline())
list1 = list(map(int, sys.stdin.readline().split()))
N = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))

c = Counter(list1)  #list1은 비교하고자 하는 배열, counter 함수는 
for i in list2:   #list2 안의 배열을 처음부터 하나씩 꺼냄
    if i in c:
        print(c[i], end = ' ')
    else:
        print(0, end = ' ') #end는 출력할 때, 끝을 공백으로 해서 끝내겠다는 의미