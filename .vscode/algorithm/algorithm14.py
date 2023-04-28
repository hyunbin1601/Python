#재귀함수 이용
#cost, 시간 복잡도 생각하며 풀기

def pibonacci(num):
    number0 = 0
    number1 = 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return pibonacci(num-1) + pibonacci(num-2)
    
a = pibonacci(int(input()))
print(a)