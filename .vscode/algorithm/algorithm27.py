import sys

croatiaword = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']  #list 만들고 for문 사용
word = sys.stdin.readline().strip()  #개행문자 처리가 중요함!

#개행문자 제거 안한 경우, word 문자열에 개행문자도 포함하는 걸로 컴퓨터가 인식함
for i in croatiaword:
    word = word.replace(i, '*')   #replace함수로 인해 변한 word값을 기존에 있던 변수에 넣는다.

#i번째 문자열을 *로 대체해서 다시 변수에 집어넣는다는 의미

 
print(len(word))
