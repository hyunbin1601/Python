import sys

number = int(sys.stdin.readline())

arr = set(map(int, sys.stdin.readline().split()))
#입력받을 정수값들을 스페이스 단위로 받아서 set로 저장
#중복값이 필요없으므로, 리스트보단 set이 시간효율적 측면에서 좋음
number2 = int(sys.stdin.readline())

arr2 = list(map(int, sys.stdin.readline().split()))

arr3 = []
for i in arr2:
    if i in arr:
        arr3.append(1)
    else:
        arr3.append(0)
print(' '.join(map(str, arr3)))


#중복값이 필요없는 배열의 경우, set을 이용하면 시간적 측면에서 많은 이드글 볼 수 있다.
#if ~ in 명령문을 통해 코드를 간편화할 수 있다. 파이썬의 장점.