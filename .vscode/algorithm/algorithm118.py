import sys
input = sys.stdin.readline

num = int(input())
lst = list(map(int, input().rstrip().split()))

max_num = max(lst)
min_num = min(lst)

print(min_num, end=' ')
print(max_num)