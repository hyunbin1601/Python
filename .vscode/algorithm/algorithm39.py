a, b = map(int, input().split())

while True:
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        print("factor")
    elif b % a != 0 and a % b == 0:
        print("multiple")
    elif b % a != 0 and a % b != 0:
        print("neither")
    
    a, b = map(int, input().split())
    
    