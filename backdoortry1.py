#서버, cnc server
#배포 -> python파일 exe 로 사용 가능
import socket #socket을 불러옴
addr = ('', 12345) #local ip는 0.0.0.0으로 고정? -> 다른 외부 서버 허용
with socket.socket(SOCKET.AF_INET, socket.SOCK_STREAM) as s:  
    s.bind(addr) #주소를 바인드함
    s.listen() #주소 바인드 될 때까지 리슨함, 기다린다는 의미
    print('cnc server is start!!')
    conn, addr = s.accept() #서버가 응답할 경우, conn과 addr로 들어옴, 클라이언트와 연결이 맺어지면 연결 정보들이 들어온다는 의미
    print('Connect by', addr) #누구랑 접속이 되었는지 확인해주는 코드
    
    while True:
        try:          #수많은 에러들이 있으므로 try exception문 사용
            #받아온 데이터를 출력함
            data = conn.recv(1024) #encoding관련 코드
            if data: #data를 받을 경우
                print(data.decode(), end='') #받아온 데이터, 즉 반환값을 출력한다
                #보낼 데이터를 전송함
                data = input()  #내가 치고 싶은 데이터를 받아줌
                conn.send(data.encode()) #보낼때는 tcp이기 때문에 반드시 enc를 해 줘야 한다.
        except Exception as e:
            print(e) #오류 날 경우, 에러문 출력
            
print("end!!!")


# Windows 명령어 익히기! 함께 털러 가보자!
            