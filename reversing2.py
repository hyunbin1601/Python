def rol(a, n): #rol(a, n) 에 x, n 에 값 입력하기
    shiftBit = a << n #rol 비트의 연산에 대한 이해 필요
    shiftBit &= 255 #shiftBit = shiftBit&255
    carryBit = a >> 8 - n  
    return shiftBit | carryBit 
#rol 계산하는 함수

def guess(c, i):
    for j in range(33, 128):   #33비트부터 시작함
        if rol(j, (i & 7)) ^ i == c:
            print(chr(j), end='') 
            break


encrypted = [] #여기에 16진수의 값들을 넣어주면 될 듯 하다.

for i in range(0, 31): #32개의 bit를 비교하는 
    guess(encrypted[i], i)