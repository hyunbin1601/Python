# 리스트에서 in, not in 은 O(N) 정도로 느리게 동작한다.
# 파이썬 set 사용하기
# 파이썬 set에서 비어있는 집합을 만들려면 set()으로 초기화를 해줘야 한다

import sys
input = sys.stdin.readline

num = int(input())
name = set()
cnt = 0

for i in range(num):
    user = input().rstrip()
    if user == "ENTER":
        cnt += len(name)
        name = set()
    else:
        name.add(user)
    
cnt += len(name)

print(cnt)