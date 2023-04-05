import sys
n = int(sys.stdin.readline())

print(sum(map(int, input())))  #sum메소드를 활용하여 안에 있는 모든 값들을 더함, int는 반환값을 정수형으로 만드는 함수, map은 반환될때 list로 반환해야 표현가능

#map함수는 대체 뭐지
##map 함수, 첫번째는 매개변수로 함수가 오고, 두번째 매개변수는 자료형이 옴 이 자료형은 반복 가능함
#sum()은 하나의 기능인듯? sum()메소드는 ()안의 값들을 모두 더해준다

#map 함수이 출력은 map 객체ㅣ므로, 객체가 출력된다