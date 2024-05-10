import sys
input = sys.stdin.readline
# 스택 배열에서 pop 함수 -> 매개변수로 index 값을 받아서 배열에서 삭제하고 출력함

n, k = map(int, input().split())
arr = [i+1 for i in range(n)]  # [1, 2, 3,4, ....]
ans = []
idx = 0

while len(arr) > 0:
    idx = (idx + k - 1) % len(arr)  # 다음에 제거될 요소의 인덱스 계산
    #len(arr) = 1일 경우, 항상 나머지(나머지 연산 : %)는 0이 되므로, 그냥 위의 식 하나로 표현 가능
    ans.append(arr.pop(idx))
        
print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print(ans[len(ans)-1], end='')
print(">", end='')
