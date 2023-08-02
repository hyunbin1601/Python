###시발 개어려움###


a, b = map(int, input().split()) #a와 b는 각각 행과 열

all = []  #전체 보드를 나타낼 리스트 board
result = []  #결과값 리스트

for _ in range(a):
    #위에서 a는 행을 의미한다
    all.append(input())  #문자열을 입력받으므로
    
for i in range(a-7):
    for j in range(b-7):
        black = 0
        white = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0:
                    if all[k][l] == 'B':
                        black += 1
                    if all[k][l] == 'W':
                        white += 1
                else:
                    if all[k][l] == 'W':
                        black += 1
                    if all[k][l] == 'B':
                        white += 1
        #for문 탈출해서 실행
        result.append(min(black, white))

print(min(result))   #result에서 가장 작은 값을 출력한다
