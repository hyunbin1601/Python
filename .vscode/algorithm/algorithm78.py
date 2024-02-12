# num = int(input())

# #알파벳 순 정렬 -> sort 이용

# arr = []
# arr2 = []  #중복 없는 버전
# arr3 = []  #중복 없는 개수 리스트
# tmp1 = []

# for i in range(num):
#     arr.append(input())
    
# for i in arr:
#     if i not in arr2:
#         arr2.append(i)

# for i in range(len(arr2)):
#     if len(arr2[i]) not in arr3:
#         arr3.append(len(arr2[i]))


# for i in range(len(arr3)):
#     tmp2 = []
#     for j in range(len(arr2)):
#         if arr3[i] == len(arr2[j]):
#             tmp2.append(arr2[j])
#     if len(tmp2) > 1:
#         tmp2.sort()
#         for k in range(len(tmp2)):
#             tmp1.append(tmp2[k])
#     else:
#         tmp1.append(tmp2[0])

# for i in range(len(tmp1)):
#     print(*tmp1[i])


num = int(input())

#알파벳 순 정렬 -> sort 이용, sort를 이용하면 길이에 상관없이 맨 앞글자의 알파벳 순서에 따라 정렬된다!

arr = []
arr2 = []

for i in range(num):
    arr.append(input())
    
arr.sort()

for i in arr:
    if i not in arr2:
        arr2.append(i)  
        
arr2.sort(key=len)

for i in arr2:
    print(i)

#길이를 활용하거나, 람다식을 활용할 수 있음
#람다식을 활용할 경우 -> key=lambda x: len(x)
