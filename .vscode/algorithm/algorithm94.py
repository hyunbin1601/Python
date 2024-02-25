#이차원 배열에서 최대최소 구하기 -> 이차원 배열 안의 배열을 따로 빼내서 일차원 배열을 만듦
#일차원 배열 안에서 max, min 함수로 최댓값 구한 후 저장, 계속 비교
#index() 함수로 해당 value의 인덱스 구하기

arr = []
max_value = 0
max_index1 = 0
max_index2 = 0

for i in range(9):
    arr.append(list(map(int, input().split())))
    

for i in range(9):
    arr2 = arr[i]
    if max(arr2) > max_value:
        max_value = max(arr2)
        max_index1 = i
        max_index2 = arr2.index(max(arr2))
        
print(max_value)
print(max_index1 + 1, end=' ')
print(max_index2 + 1)

    
        
