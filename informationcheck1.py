#아까 컴퓨터 정보 출력 코드를 정리해서, 필요 정보만 출력하는 코드를 생성한다.
import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)
print(f"cpu 속도: {cpu_current_ghz}GHz") #f {}를 이용해서, print를 통해 출력할 때 변수값을 대입해서 출력할 수 있다.
cpu_core = psutil.cpu_count(logical=False) #psutil의 부가기능 중 cpu_count라는 기능이 있나봄...
print(f"코어: {cpu_core}개")

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3) #1024를 세제곱한다니 이건 원리를 알아야 하는겨....메모리의 총량을 구하는 코드

print(f"메모리 : {memory_total}GB") #''로 써도 상관없다. 구별문자? 만 나중에 알아보도록 하자.
disk = psutil.disk_partitions() #disk의 크기 출력
for p in disk: 
    print(p.mountpoint, p.fstype, end = ' ') #for 함수의 메소드인가...? mountpoint가 뭐지...
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024 ** 3)
    print(f'디스크 크기: {disk_total}GB')

net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024**2, 1) #네트워크를 통해 보내고 받은 데이터를 크기를 MB단위로 출력한다. 보내고 받은 데이터는 누적 데이터의 값
recv = round(net.bytes_recv / 1024 ** 2, 1)
print(f'보내기: {sent}MB 받기: {recv}MB') #round는 반올림 메소드를 의미함. 기본적으로 내장되어있는 메소드

##왜 내 노트북 이리도 연약한 것....? 미안해 너무 혹사시켜서....ㅎㅎ
