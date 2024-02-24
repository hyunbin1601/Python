#배열의 음수 인덱스 생각해보기
# https://dojang.io/mod/page/view.php?id=2207
# 배열에서 음수란, 뒤에서부터 센다는 의미다. -1일 경우 뒤에서 첫번째, -2일 경우 뒤에서 두번째....etc
import sys

while True:
    word = sys.stdin.readline()   #sys.stdin.readline()은 줄바꿈 문자도 받기 때문에 따로 표시
    stack = []
    
    if word == ".\n":
        break
    else:
        for i in word:
            if i == "(" or i == "[":
                stack.append(i)
            elif i == ")":
                if stack:  #stack이 안비워져있을경우
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
                        break
                else:
                    stack.append(i)
                    break
            elif i == "]":
                if stack:
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        stack.append(i)
                        break
                else:
                    stack.append(i)
                    break
                
    if stack:  #stack이 안비어져있는경우
        print('no')
    else:
        print('yes')
                