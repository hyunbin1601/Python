num = int(input())
arr=[]

for i in range(num):
    number = int(input())
    if number == 0:
        if len(arr) != 0:
            arr.pop()
    else:
        arr.append(number)

print(sum(arr))