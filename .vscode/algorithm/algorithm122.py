import sys
import itertools

n, m = map(int, input().split())
perm = [i+1 for i in range(n)]

for i in itertools.permutations(perm, m):
    perm_iter = list(i)
    for j in range(len(perm_iter)):
        print(perm_iter[j], end=' ')
    print()
    
#위는 파이썬의 itertool 라이브러리를 사용해서 간단하게 푼 예시
