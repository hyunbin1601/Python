# 좌표압축 알고리즘

num = int(input())
arr = list(map(int, input().split()))

arr2 = list(set(arr)).sort()

dic = {arr2[i]:i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end=' ')

# 좀 공부가 필요할듯
    
    






