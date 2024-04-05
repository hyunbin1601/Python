import sys
input = sys.stdin.readline

num = int(input())
arr = []
arr2 = {}
max_value = 0

for _ in range(num):
    n = int(input())
    arr.append(n)
    if not n in arr2:
        arr2[n] = 1
    else:
        arr2[n] += 1

mid = round(len(arr) / 2)  #차피 몫 값만 필요함

avg = round(sum(arr) / len(arr))
arr.sort()
mid_num = arr[mid]

ran = max(arr) - min(arr)

##최빈값 구하기##


# for i in range(len(arr)):
#     arr2[arr[i]] = arr.count(arr[i])  #키값은 중복이 되지 않는다.

# arr2_reverse = {v:k for k,v in arr2.items()}    
max_arr2 = max(arr2.values())
# arr2_keys = list(arr2.keys())
# arr2_values = list(arr2.values())
arr2_list = [key for key, val in arr2.items() if val == max_arr2]
if len(arr2_list) > 1:
    arr2_list.sort()
    max_value = arr2_list[1]
else:
    max_value = arr2_list[0]
    
print(avg)
print(mid_num)
print(max_value)
print(ran)
    

