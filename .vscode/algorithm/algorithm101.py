a, b = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_set = set(arr1)
arr2_set = set(arr2)

rem1 = arr1_set - arr2_set
rem2 = arr2_set - arr1_set

print(len(rem1) + len(rem2))



