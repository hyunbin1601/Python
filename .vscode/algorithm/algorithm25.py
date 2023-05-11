import sys

word = sys.stdin.readline().upper()
#set이용, set은 자료형중 하나인데 중복을 허용치 않음....
onlyoneword = list(set(word))   #set으로 중복을 없앤 후 list에 값을 넣는다

a = []  #문자의 개수가 들어있는 리스트
for i in onlyoneword:
    a.append(word.count(i))
    
#파이썬 내장함수를 통해 쉽게 해결할 수 있다
#내장함수 max 이용
#max, min 함수는 그 리스트, 튜플, 세트에 들어있는 숫자 중 제일 큰 숫자를 추출한
if a.count(max(a)) > 1:
    print('?')
else:
    maxindex = a.index(max(a))
    print(onlyoneword[maxindex])
        


