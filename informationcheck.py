#cpu 속도,물리 코어수, 메모리, 디스크, 네트워크 정보 확인 코드
import psutil #psutil 라이브러리를 가져온다는 의미
cpu = psutil.cpu_freq() #변수를 선언할 때, 앞에서 변수의 형태를 굳이 선언하지 않아도 된다 psutil 라이브러리에서 메소드 값을 가져온다.
print(cpu) #cpu 속도 출력

cpu_core = psutil.cpu_count(logical = False)  #cpu 물리코어 수 출력
print(cpu_core)

memory = psutil.virtual_memory() #virtual_memory 메소드를 라이브러리를 가져옴 메모리의 정보를 출력함
print(memory)

disk = psutil.disk_partitions() #디스크의 정보를 출력함
print(disk)

net = psutil.net_io_counters()  #네트워크를 통해 보내고 받은 데어터량 출력
print(net)