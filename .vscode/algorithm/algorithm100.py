import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
arr = deque()
for i in range(n):
    arr.append(i+1)
ans = []

while len(arr) > 0:
    if len(arr) < k:
        idx = k % len(arr) - 1
    else:
        idx = k-1
    ans.append(str(arr[idx]))
    arr.rotate(-idx)
                
        
answer = ", ".join(ans)
print("<" + answer + ">")        