
a, b = map(int, input().split()) #2개의 값이므로, 각각의 변수에 넣는다.
#list는 append로 붙인다.

A = [[0 for i in range(b)] for j in range(a)]
B = [[0 for i in range(b)] for j in range(a)]

for i in range(a):
    A[i] = list(map(int, input().split()))
    
for i in range(a):
    B[i] = list(map(int, input().split()))
    
for i in range(a):
    for j in range(b):
        A[i][j] += B[i][j]
        print(A[i][j], end = ' ')
        
    print()




# N, M = map(int, input().split())

# A = [[0 for i in range(M)] for j in range(N)] #2차원 배열
# B = [[0 for i in range(M)] for j in range(N)]

# for i in range(0, N):
# 	A[i] = list(map(int, input().split())) #대괄호 -> 리스트의 형태

# for i in range(0, N):
# 	B[i] = list(map(int, input().split()))

# for i in range(0, N):
# 	for j in range(0, M):
# 		A[i][j] += B[i][j]
# 		print(A[i][j], end = " ")
# 	print()

    