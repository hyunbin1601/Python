n, m = map(int, input().split())

if m - 45 >= 0:
    print(n, end=' ')
    print(m-45)
else:
    if n == 0:
        print(23, end=' ')
        print(60-(45-m))
    else:
        print(n-1, end=' ')
        print(60-(45-m))