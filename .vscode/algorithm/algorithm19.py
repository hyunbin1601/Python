#첫째줄 -> 가지고 있는 카드의 개수
#둘째줄 -> 숫자 카드에 적혀있는 정수
#셋째줄 -> 입력할 수의 개수
#넷째줄 -> 입력할 숫자
#이진탐색으로 문제풀기
#a는 미리 정렬된 후 함수에 들어간다
#파이썬의 기능 중 count 함수를 이용해서 그 개수를 구하기
def binary_serch(a, x, start, end):  #a는 탐색 대상 리스트, x는 그 리스트에서 찾고자 하는 값
    if start>end:
        return 0 #0은 false를 의미한다!
    mid = (start+end)//2
    if a[mid] == x:
        return a[start:end+1].count(x)
    elif a[mid] > x:  #m번의 값이 x보다 클 경우
        return binary_serch(a, x, start, mid-1)
    elif a[mid] < x:
        return binary_serch(a, x, mid+1, end)
n = int(input())
a = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))
array.sort()

for i in array:
    if binary_serch(array, i, 0, n-1):
        print()
            
    




    
        