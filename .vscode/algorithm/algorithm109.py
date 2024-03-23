import sys

input = sys.stdin.readline

def cantoa(n):
    if n == 1:
        return "-"   #return을 만나면 함수가 마무리된다
    left = cantoa(n//3)   #n을 3으로 나눈 몫
    center = " " * (n//3)
    return left + center + left


while True:
    try:
        num = int(input())
        rst = cantoa(3**num)
        print(rst)
    except:
        break
    

        
    