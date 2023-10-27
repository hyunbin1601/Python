num = input()  #문자열을 입력받음

a = []  #리스트 선언

for i in num:
    a.append(int(i))
    
a.sort(reverse=True)

str1 = ''

for i in range(len(a)):
    str1 = str1 + str(a[i])
    
print(str1)


    