class Greet():
    def hello(self):   #여기서 self란 자시 자신으로, 클래스 메서드를 만들 때 꼭 붙여줘야 한다 이렇게 -> (self)
        print("hello")
    def hi(self):
        print("hi")
        
human1 = Greet() #__init__ 함수가 없으므로 객체를 생성한다고 해서 바로 실행되지는 않는다.
human2 = Greet()
human1.hello()
human1.hi()
human2.hello()
human2.hi()

class Student():
    def __init__(self, name, age, like): #객체를 만들 때 자동으로 동작하는 메소드로, Student()로 객체를 부르면 바로 실행된다. 아래 예시를 보자.
        self.name = name
        self.age = age
        self.like = like
    def studentInfo(self): 
        print(f"이름: {self.name}")  #f ~ {변수}를 통해 print 출력할때 변수를 출력할 수 있다
        
h1 = Student("안철수", 17, "축구") #정수형, 실수형, 문자형은 파이썬이 알아서 인식함,,,
h1.studentInfo()      #위의 Student()클래스에 __init__ 함수가 있어서 부른 순간 바로 실행되서 클래스 변수에 변수값이 넣어져서, 이 함수를 실행하면 제대로 출력될 것임

#클래스는 상속도 있음, 자바랑 다르게 간단데스
#참고로, 파이썬은 자동적으로 형변환이 되지 않기 때문에 int(변수) 이런 식으로 강제로 형변환을 해 줘야 한다. 참고로 입력값은 모두 기본적으로 문자형으로 컴퓨터가 받아들인다. 강제로 형변환 필요
class Mother():
    def charactersitic(self): #클래스의 메소드는 매개변수가 있든 없든 무조건 self를 넣어야함!
        print("키가 크다")
        print("공부를 잘한다")
class Daughter(Mother): ##이렇게 넣어서 Mother를 상속받는다, 부모의 메소드를 불러오고 싶으면 super 붙이기!
    def characteristic(self): #부모 메소드의 이름과 같아도 된다. 자세한건 하면서 익히자
        super().charactersitic()  #super가 앞에 붙으면 부모 메소드를 불러와서 실행한다는 의미
        print("운동을 잘한다")
        
엄마 = Mother()
딸 = Daughter()

엄마.charactersitic()
딸.characteristic()  #엄마의 메소드에 딸의 메소드값을 붙여 총 3개의 출력문이 튀어나옴

