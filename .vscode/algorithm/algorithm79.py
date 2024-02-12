# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
# 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

num = int(input())
arr = []


for i in range(num):
    people = []
    a, b = map(str, input().split())
    people.append(int(a))
    people.append(b)
    arr.append(people)
    
arr.sort(key=lambda x:x[0])

for i in range(num):
    print(*arr[i])