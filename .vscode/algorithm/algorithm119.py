n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())   #좌표값
    for j in range(y, y+10):
        for k in range(x, x+10):
            if [k, j] not in arr:
                arr.append([k, j])

print(len(arr))