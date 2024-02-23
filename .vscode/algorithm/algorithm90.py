#13909, 아직 해결 못함
#문제의 접근 포인트를 다르게 설정해야함, 값이 변화하는 지점 생각하기

# num = int(input())

# array = [True for i in range(1, num+1)]
# cnt = 0

# for i in range(2, num+1):
#     j = 1
#     while i * j <= num:
#         if array[i * j] == True:
#             array[i * j] == False
#         else:
#             array[i * j] == True
#         j += 1

# for i in range(1, num+1):
#     if array[i] == True:
#         cnt += 1
# print(cnt)

num = int(input())
cnt = 1
result = 0
while num >= cnt ** 2:
    cnt += 1
    result += 1
    
print(result)