#재귀함수 알고리즘
#재귀를 이용한 팰린드롬 함수 여부

number = int(input())


def recursion(s, l, r):
    global cnt  #함수 내의 변수를 전역변수로 설정해 준다
    cnt += 1
    if l >= r: #l은 처음값, r은 마지막값, 그러므로 같거나 처음값보다 작으면 오류/ 아님
        return 1   #1인 경우, 팰린드롬 함수
    elif s[l] != s[r]: 
        return 0  #0인 경우, 아니다
    else:  #같을 경우
        return recursion(s, l+1, r-1)  

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)  #처음에는 첫번째와 마지막을 비교
#파이썬에서 인덱스는 0부터 시작


    
for i in range(number):
    cnt = 0   #문자열을 입력받을 때마다 초기화
    print(isPalindrome(input()), cnt)  #rstrip을 안쓰는 방법..?

    

    

