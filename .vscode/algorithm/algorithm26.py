import sys

c = int(sys.stdin.readline())  #문자열을 받을 때, 개행문자를 포함해서 입력값을 받는다
for _ in range(c):
    num = list(map(int, sys.stdin.readline().split())) #리스트에 값을 넣는다
    avg = sum(num[1:]) / num[0]   #num[1:]은 인덱스 1부터 끝까지
    cnt = 0  #평균을 넘는 학생의 수
    for i in num[1:]:
        if i > avg:
            cnt += 1
    rate = cnt/num[0] * 100
    #round 함수의 경우, 정수형의 변수에 대해 소수점의 자릿수를 출력할 수 없다
    print(f"{rate:.3f}%")
