n, m = map(int, input().split())

lst = []

result = [x for x in range(1, n+1)]

def dfs():
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return
    else:
        for i in range(1, n+1):
            if i not in lst:
                lst.append(i)
                dfs()
            