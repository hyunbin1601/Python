

number = int(input())


cnt1 = number

for _ in range(number):
    cnt2 = 0  #해당 문자열을 받고 바로 cnt를 계산한다
    word = input()
    for i in range(len(word)-1):  #index는 0부터 시작하므로
        if word[i] == word[i+1]:
            pass  #그냥 넘어가, 아무 동작을 하지 않고 다음 코드를 실행한다는 의미
        elif word[i] in word[i+1:]:
            cnt1 -= 1
            break   #만약 한번 더 존재할 경우, 총 2번이나 더 깎이는 셈이므로 break를 해주고 해당 반복문에서 탈출해야한다
    
print(cnt1)        