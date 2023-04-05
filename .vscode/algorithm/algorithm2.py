'''testcase = int(input())

for i in range(testcase):
    word = str(input())   #str 라고 형 선언해줘야 하나...?
    print(word[0] + word[-1])  ##...??파이썬의 세계는 참 간단하다..            
            
 '''           
# 그냥 알고리즘만 맞아도 맞게처리하는듯, 매커니즘이 같으면 같다고 하는건가?

class outputword():
    print("test case 입력")
    
    def __init__(self):
        test = int(input()) #입력값을 int형으로 바꿔줌
        j = 1
        case = []
        countfirst = []
        countlast = []
        print("문자열을 입력하세요")
        for i in range(test):
            case[i] = input()
            countfirst[i] = case[i][0]
            countlast[i] = case[i][-1]
            j = j+1
            
        for i in range(j-1):
            print(countfirst[i] + countlast[i])
            
            
outputword()   

##내가 너무 복잡하게 생각하는 건가...?
##이런 시발

        