#brute force를 이용하는 문제
a, b = map(int, input().split())  #값 2개를 입력받을 때는 ㄱㅊ
c = list(map(input().split()))   #split은 메소드이다!!
#c에 들어가는 값은 정수이므로, int 함수를 통해 형변환 해줘야함
#c는 split에 의해 리스트를 가지는 변수이다
#c에는 여러개의 숫자를 입력받아, 여기서 3개를 골라서 더해 가장 가까운 수를 만드는것

result = 0  #문제 조건에 적합한 수를 저장하여 반환하기 위한 변
#0은 왜 대입함...?
for i in range(a):
    for j in range(i+1, a):
        #2, 3, 4,, .....a까지의 숫자동안 반복함
        for k in range(j+1, a):
            if c[i] + c[j] + c[k] > b:
                continue #continue는 건너뛴다는 의미
            else:
                result = max(result, c[i]+c[j]+c[k])
                
#3개의 카드를 뽑아야 하며, 이를 위해 3중 for문이 필요함               
print(result)
#모든 경우의 수를 다 뒤져봐야 하는 완전 탐색 문제
#파이썬의 인덱스는 당연히 0부터 시작한다, for문이나 while문도 마찬가지
#3개의 경우의 수 0, 1, 2 / 0, 1 ,3 / 0, 1, 4 .....이렇게 이어진다
#continue는 해당 조건문을 건너뛰고 다시 처음 반복문으로 돌아온다는 의미!
#break는 해당 조건문과 반복문에서 아예 벗어난다는 의미
#max 함수는 result와 지금 3개의 더한 값 중에서 더 큰것을 출력하는 메소