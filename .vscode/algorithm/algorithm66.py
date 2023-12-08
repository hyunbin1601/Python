x, y, w, h = map(int, input().split())

a = w-x
b = h-y

arr = []
arr.append(x)
arr.append(y)
arr.append(a)
arr.append(b)

num = arr[0]

for i in arr:
    if num >= i:
        num = i

print(num)

            