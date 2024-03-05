import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = set()
arr2 = set()
for i in range(n):
    arr.add(input().rstrip())
    
for i in range(m):
    arr2.add(input().rstrip())
    
arr3 = list(arr & arr2)

arr3.sort()

print(len(arr3))
for i in range(len(arr3)):
    print(arr3[i])