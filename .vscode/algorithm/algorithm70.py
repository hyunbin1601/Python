n, m = map(int, input().split())
k = int(input())
p = 0
l = 0

# n은 시간, m은 분, k는 추가되는 시간

if m + k < 60:
    print(n, end=' ')
    print(m+k)
else:
    p = (m+k) // 60
    l = (m+k) % 60
    if n + p > 23:
        print(n+p-24, end=' ')
        print(l)
    else:
        print(n+p, end= ' ')
        print(l)