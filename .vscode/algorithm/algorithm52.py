import sys

n = int(sys.stdin.readline())

num = [0]*10001  #리스트 모두에 0을 할당, 총 10001개를 생성

for _ in range(n):  #굳이 인덱스 번호표시가 필요하지 않으므로
    num[int(sys.stdin.readline())] += 1  #반복해서 나올 경우, 1보다 클 것이므로 두번 이상 출력됨, 처음 수는 모두 0이므
    

for i in range(10001):   #알아서 오름차순으로 분류되므로
    if num[i] != 0:
        for j in range(num[i]):
            print(i)

