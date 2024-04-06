# 첫째 줄에는 영어 지문에 나오는 단어의 개수 
# $N$과 외울 단어의 길이 기준이 되는 
# $M$이 공백으로 구분되어 주어진다. (
# $1 \leq N \leq 100\,000$, 
# $1 \leq M \leq 10$)

# 둘째 줄부터 
# $N+1$번째 줄까지 외울 단어를 입력받는다. 이때의 입력은 알파벳 소문자로만 주어지며 단어의 길이는 
# $10$을 넘지 않는다.

# 단어장에 단어가 반드시 1개 이상 존재하는 입력만 주어진다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
voc = {}

for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if not word in voc:
            voc[word] = 1
        else:
            voc[word] += 1

#딕셔너리 value 값 오름차순 정렬
voc_sort = sorted(voc.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in range(len(voc_sort)):
    print(voc_sort[i][0])


        
