def func(): #함수의 이름은 func이고, 인자값을 받을 매개변수는 존재하지 않는다.
    print("안녕하세요")
    print("파이썬과 40개의 작품들입니다.")
    
func()  #위에서 만든 함수를 부름

def func1():
    print("안녕하세요")
    print("파이썬 초보 임현빈데스.")
    print("요로시쿠오네가이시마스")
    
for i in range(3):
    func1()   #0,1,2 즉 3번 반복한다는 의미이다.
    #func1()을 3번 불렀으니 3번반복해서 함수가 실행된다.

def funcAdd(a, b):
    #인자값을 받아 매개변수에 저장하고, 매개변수를 이용하여 return문을 이용하여 함수를 호출하면 호출값을 출력함
    return a+b #a+b의 값을 반환, 즉 불러낸 변수에 저장함

c = funcAdd(3, 4)  
print(c)  #파이썬은 알아서 줄바꿈 기능이 있는 듯 하다.
#파이썬은 또한, 여러개의 값을 한꺼번에 반환 가능하다. 함 살펴보자

def funcAddMux(a, b):
    add = a+b
    mux = a*b
    return add, mux  #2개의 값을 반환한다. 대신, 아래에서 보는 것처럼 각각의 반환값을 저장할 변수들이 각각 존재해야 한다

a, b = funcAddMux(1, 3)
print(a, b)