

num = int(input())   #구하고자 하는 값의 분해합을 입력

result = 0
tmp = 0

for j in range(1, num + 1):   #j에 1부터 num까지의 숫자가 올 수 있다는 의미
    n = list(map(int, str(j)))  #j를 문자열로 치환한 후, 각 자릿수르 다시 인수로 바꾼 후 리스트에 저장
    result = sum(n) + j   #해당 숫자는 더해야 하므로
    if result == num:
        tmp = j
        break
    
if tmp != 0:
    print(tmp)
else:
    print(0)
    

    
        