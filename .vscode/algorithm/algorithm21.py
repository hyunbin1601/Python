import sys

inputnumber = list(map(int, sys.stdin.readline().split()))
#스페이스바를 기준으로 리스트에 원소값을 넣는다

king = str(1 - inputnumber[0])
queen = str(1 - inputnumber[1])
luuk = str(2 - inputnumber[2])
bishop = str(2 - inputnumber[3])
knight = str(2 - inputnumber[4])
pone = str(8 - inputnumber[5])

print(king + " " + queen + " " + luuk + " " + bishop + " " + knight + " " + pone)


    