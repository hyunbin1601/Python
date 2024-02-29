#파이썬 라이브러리의 deque 라이브러리 이용
#deque 라이브러리는 수행속도가 리스트에 비해 월등히 빠름
#rotate 문제에서 강점을 보임

from collections import deque
import sys
input = sys.stdin.readline

num = int(input())  #rstrip을 이용해야 하는 이유 -> \n이 함께 들어가기 때문에
arr = deque([])

for i in range(num):
    ans = list(map(str, input().split()))
    if ans[0] == "push":
        arr.append(int(ans[1]))   #오른쪽 끝에서 새로 원소가 붙음 -> [1, 2,]에서 3 append면 [1, 2, 3] 이렇게
    elif ans[0] == "front":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[0])
    elif ans[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif ans[0] == "size":
        print(len(arr))
    elif ans[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())   #[1, 2, 3] 여기서 popleft를 할 경우 1이 빠져나옴(가장 왼쪽끝), 반대로 pop을 할 경우 3이 빠져나옴(가장 오른쪽 끝)
    else:
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
        


