n, m = map(int, input().split())

a = list(map(int, input().split()))   #스페이스바 단위로 입력값을 받고, 리스트에 저장한다.

a.sort()  #일단 오름차순으로 정리

print(a[n-m])