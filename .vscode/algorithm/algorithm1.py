class Stringword():
    def __init__(self):
        word = input()  #입력값을 받음
        num = len(word)
        print(num)
    

Stringword()   #__init__을 이용하면 클래스 명만 불러도 바로 init 메소드를 실행시킬 수 있다.