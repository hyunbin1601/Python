a, b = map(int, input().split())  #공백 스페이스단위로 끊어서 값을 입력받음
#a에는 배열의 크기, b에는 저장횟수
#합병정렬 문제
#재귀함수는 봐도봐도 이해가 안되노...

#solution -> 병합정렬 로직 참고, 빈 배열을 만들고 정렬되는 순서대로 추가만 해주면 끝

def merge_sort(s):
    if len(s) == 1:
        return s
    
    mid = (len(s)+1)//2 #내림값으로 출력된다
    left = merge_sort(s[:mid]) #mid-1까지의 값
    right = merge_sort(s[mid:])
    
    i, j = 0, 0 #변수에 각각 값을 넣음
    s2 = []  #하나의 리스트를 더 만듦
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            s2.append(left[i])
            ans.append(left[i])
            i += 1
        else:
            s2.append(right[i])
            ans.append(right[i])
            j += 1
    while i<len(left):
        s2.append(left[i])
        ans.append(left[i])
        i += 1
    while j<len(right):
        s2.append(right[j])
        ans.append(right[j])
        j += 1
    return s2

k = list(map(int,input().split())) #공백 단위로 값을 리스트에 저장함
ans = []

merge_sort(k)
if len(ans) >= b:
    print(ans[b-1])
else:
    print("-1")
    


            

