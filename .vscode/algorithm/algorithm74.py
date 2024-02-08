# 삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의한다.

# Equilateral :  세 변의 길이가 모두 같은 경우
# Isosceles : 두 변의 길이만 같은 경우
# Scalene : 세 변의 길이가 모두 다른 경우
# 단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.

# 세 변의 길이가 주어질 때 위 정의에 따른 결과를 출력하시오.

while(True):
    arr=list(map(int, input().split()))
    max_num = max(arr)
    min_num = min(arr)
    arr.remove(max_num)
    arr.remove(min_num)
    mid_num = arr[0]
    if max_num == 0 or mid_num ==0 or min_num == 0:
        break
    elif max_num >= mid_num + min_num:
        print("Invalid")
    else:
        if max_num == mid_num == min_num:
            print("Equilateral")
        elif max_num == mid_num or max_num == min_num or mid_num == min_num:
            print("Isosceles")
        else:
            print("Scalene")
        
        
        