number = list(map(int, input().split()))
if number[1] == 0:
    exit(0)
else:
    result = number[0] / number[1]
    print(result)