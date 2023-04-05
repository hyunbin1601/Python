# word = input()   #비교할 문자, 단어 s라고 보면 됨?
# #단어 입력받음
# #단어 입력받은 후, 위치에 따라 입력값 다름
# '''알파벳 소문자로만 이루어진 단어 S가 주어진다. 
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 
# 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.'''
# word2 = input()   #1인지 -1인지 출력할 문자
# cnt = -1
# num = 0
# wordlist = []
# #word의 단어들과 word2의 단어들을 비교한다
# #word2의 문자 각 하나하나를 word의 문자들을 모두 비교해 보면서, 똑같은 문자가 있다면 그 문자의 위치를 출력하고, 없으면
# #-1을 출력한다
# '''
# for i in word2:
#     for j in word:
#         if i==j:
#             cnt += 1
#             print(cnt)
#         #i라는 문자 하나에 대해서 모든 word의 구성원들과 비교한다.
#  '''  
# for j in word:
#     wordlist[num] = j
#     num += 1     
# #num과 wordlist[] list로 하나하나 비교
# for i in word2:
#     #i는 word2 안에 있는 문자
#     for k in range(num):   #index는 0부터 시작한다
#         if worldlist[k] == i:
#             print(k)
#             cnt += 1
#             break   #그래야 for문을 탈출함
        
#     if cnt<0:
#         print(cnt)
#     cnt = -1 #다시 초기화
    
'''tlqkf'''
s = list(input())    #list를 통해 입력받은 값을 문자열 기준으로 하나하나씩 분리해서 각각 인덱스를 부여해서 리스트에 넣는다.
c = 'abcdefghijklmnopqrstuvwxyz'     #정 안돼면 c를 입력값으로 받아도 되고

for i in c:
    if i in s:   #s 안에 i라는 문자열이 있다고 가정할 경우
        print(s.index(i), end = ' ')   #list의 경우, index값을 그 안의 문자열(key)값을 통해 알아낼 수 있나봄
    else:
        print(-1, end=' ')
    
#index() 함수는 value 값을 통해 인덱스 값을 출력해 주는 함수이다.  