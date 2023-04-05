'''문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

출력
각 테스트 케이스에 대해 P를 출력한다.'''
# r = int(input())
# s = list(input())  #입력값을 list로 입력받음
# for i in s:  #s안에 있는 글자 처음부터 끝까지
#     for j in range(r):    #0부터 r까지 계속해서 반복한다
#         print(i)    #r번동안 계속 출력

#위에게 틀린 이유 -> 공백을 기준으로 나눠야 하는데 나누질 못함....
#파이썬에서 공백을 기준으로 문자열을 나누는 함수 -> split()

'''
2 2개의 입력값을 받으면, 2번 반복하겠다는 의미다.
3 ABC  2개의 인자값을 받는다. 파이썬은 2개의 인자값을 이렇게 받을 수 있다
5 /HTP
'''
# t = int(input())
# for i in range(t):  #t번 반복한다는 의미
#     num, s = input().split()  #split()에 그 어떠한 인자도 들어가 있지 않다-> 공백을 기준으로 문자열을 자르겠다.
#     for j in s:
#         #s안에 있는 문자열을 하나하나씩 살펴보겠다
#         for k in range(int(num)):
#             print(j)
t = int(input())
for i in range(t):  
    num, s = input().split()  
    text = ''
    for j in s:
        
        text += int(num) * j   #파이썬 개념 또 정리하기! 숫자 * 문자열은 문자열을 그 수만큼 반복해서 입력된다는 의미이다! 
    print(text)