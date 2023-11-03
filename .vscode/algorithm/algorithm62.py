# 층 기준으로 계산하기

num = int(input())
initial = 1
cut = 0
cnt = 1

if num == 1 :
    print(1)
else:
    while initial <= num:
        cut = initial + 6 * cnt
        if (initial <= num <= cut):
            cnt += 1
            break
        elif (num > cut):
            initial = cut
            cnt += 1
    print(cnt)
        