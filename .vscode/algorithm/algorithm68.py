x = []
y = []

for _ in range(3):
    x_num, y_num = map(int, input().split())
    x.append(x_num)
    y.append(y_num)

x_max = max(x)
y_max = max(y)
x_min = min(x)
y_min = min(y)

if x.count(x_max) == 1:
    if y.count(y_max) == 1:
        print(x_max, end = ' ')
        print(y_max, end= ' ')
    elif y.count(y_max) == 2:
        print(x_max, end = ' ')
        print(y_min, end= ' ')
elif x.count(x_max) == 2:
    if y.count(y_max) == 1:
        print(x_min, end = ' ')
        print(y_max, end= ' ')
    elif y.count(y_max) == 2:
        print(x_min, end = ' ')
        print(y_min, end= ' ')       