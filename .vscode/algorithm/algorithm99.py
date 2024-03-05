import sys
from collections import deque

input = sys.stdin.readline

num = int(input())
cnt = 0

deq = deque([])

for i in range(num):
    deq.append(i+1)
    
while True:
    if len(deq) == 1:
        break
    else:
        if (cnt+1) % 2 != 0:
            deq.popleft()
            cnt += 1
        else:
            newnum = deq.popleft()
            deq.append(newnum)
            cnt += 1
        
print(deq[0])
    

    
        
    
