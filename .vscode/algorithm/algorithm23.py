

n, m = map(int, input().split())

box = [i+1 for i in range(n)] #list안에 for문을 포함한다, list comprehension이라고도 함
#for i in range(n)에서 i값의 1만큼 더한 값만큼 리스트에 담겠다는 의미

#list 사용하는건가?

for _ in range(m):      #그냥 인덱스 없이 m번 반복한다는 의미이다.
    i, j, k = map(int, input().split())
    box[i-1:j] = box[k-1:j] + box[i-1:k-1]
    
print(*box)   #list를 한줄에 한번에 출력할 수 있다. 
# *이 없어도 되지만 *을 붙여주면 대괄호 '[]' 없이 한번에 출력이 가능하다!

    