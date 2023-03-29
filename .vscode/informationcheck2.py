#1초당 반복해서 정보를 출력하는 코드

import psutil
curr_sent = 0 #보내는값
curr_rect = 0  #받는값

prev_sent = 0
prev_rect = 0

while True:
    #break 걸리기 전까지 무한반복하는 반복문
    cpu_p = psutil.cpu_percent(interval = 1) #1초 간격으로 cpu의 퍼센트? 사용량?을 출력한다
    print(f'CPU 사용량: {cpu_p}%')
    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024**3, 1)  #round(해당값 , 1) -> 해당값을 소수점 첫째 자리까지 반올림해서 출력한다는 의미, 다르게 말해서 두번째 자리에서 반올림해서 첫번째 자리까지 나타낸다는 의미
    print(f'사용 가능한 메모리: {memory_avail}GB') #psutil.virtual_memory에서 메소드를 또 가지고 와서 변수값에 집어넣음
    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent / 1024 **2
    curr_recv = net.bytes_recv / 1024 **2
    sent= round(curr_sent - prev_sent, 1)
    recv =  round(curr_rect - prev_rect, 1)
    print(f'보내기: {sent}MB 받기: {recv}MB')
    prev_sent = curr_sent
    prev_recv = curr_recv
    