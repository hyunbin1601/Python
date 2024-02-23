import sys

num = int(sys.stdin.readline())
stack = []

for i in range(num):
    array = list(map(int, sys.stdin.readline().split()))
    if array[0] == 1:
        stack.append(array[1])
    elif array[0] == 2:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif array[0] == 3:
        print(len(stack))
    elif array[0] == 4:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[len(stack)-1])        