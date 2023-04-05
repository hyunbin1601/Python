# import random   #random 라이브러리를 import하여 사용함, random 라이브러리는 무작위 값을 반환하는 기능이 있다
# print(random.randint(1, 100))


# import random as rd
# # random 라이브러리 rd의 이름으로 불러옴
# print(rd.randint(1, 100))   #rd라는 이름으로 라이브러리에서 함수(메소드)를 불러올 수 있다

# from random import randint  #random이라는 거대한 라이브러리에서 randint라는 메소드를 가져온다
# print(randint(1, 100))

#*를 사용하여 모든 기능을 불러올 수 있다~
from random import *  #random에서 모든 함수를 불러옴
print(randint(1, 100))    #개인적으로 이거 편해서 이렇게 쓰는게 좋긴함....대체 뭘쓸지 몰라ㅎ
