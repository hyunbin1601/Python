cnt = int(input())
x = []
y = []
x_num = 0
y_num = 0

for _ in range(cnt):
    x_num, y_num = map(int, input().split())
    x.append(x_num)
    y.append(y_num)

x_max = int(max(x))
y_max = int(max(y))
x_min = int(min(x))
y_min = int(min(y))

if cnt == 1:
    print(0)
else:
    x_length = x_max - x_min
    y_length = y_max - y_min
    
    print(x_length * y_length)