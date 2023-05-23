import sys


sum = 0
avg = 0
cnt = 0

for i in range(20):
    num = list(map(str, sys.stdin.readline().split()))
    if num[2] == 'A+':
        sum = sum + float(num[1])*4.5
        cnt = cnt + float(num[1])
    elif num[2] == 'A0':
        sum = sum + float(num[1])*4.0
        cnt = cnt + float(num[1])
    elif num[2] == 'B+':
        sum = sum + float(num[1])*3.5
        cnt = cnt + float(num[1])
    elif num[2] == 'B0':
        sum = sum + float(num[1])*3.0
        cnt = cnt + float(num[1])
    elif num[2] == 'C+':
        sum = sum + float(num[1])*2.5
        cnt = cnt + float(num[1])
    elif num[2] == 'C0':
        sum = sum + float(num[1])*2.0
        cnt = cnt + float(num[1])
    elif num[2] == 'D+':
        sum = sum + float(num[1])*1.5
        cnt = cnt + float(num[1])
    elif num[2] == 'D0':
        sum = sum + float(num[1])*1.0
        cnt = cnt + float(num[1])
    elif num[2] == 'F':
        sum = sum + float(num[1])*0.0
        cnt = cnt + float(num[1])
    else:
        pass
        
avg = sum / cnt
print('%.3f' % avg)