import sys
import math

num = int(sys.stdin.readline())

def small_prime(number):
    flag = True
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            flag = False
            break
    return flag

for i in range(num):
    number = int(sys.stdin.readline())
    while(True):
        if number == 0 or number == 1:
            print(2)
            break
        else:
            if(small_prime(number)):
                print(number)
                break
            else:
                number += 1
                

