#문자열 뒤집기 -> str[::-1]로 리버스가 가능하다!

a, b = map(str, input().split())

a_num = int(a[::-1])
b_num = int(b[::-1])

if a_num > b_num:
    print(a_num)
else:
    print(b_num)

