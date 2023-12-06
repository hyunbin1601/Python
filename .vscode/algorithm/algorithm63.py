num = int(input())
line = 1
arr1 = 0
arr2 = 0
# num는 내가 찾을 순번, line은 몇번째 줄에 있는지

while line < num:   #line의 값이 num보다 작을 때까진 계속 반복
    num -= line
    line += 1
    

if line % 2 == 0:
    arr1 = num
    arr2 = line - num + 1 
    print(f'{arr1}/{arr2}')

else:
    arr1 = line - num + 1
    arr2 = num
    print(f'{arr1}/{arr2}')