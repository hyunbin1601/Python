num = int(input())
company = dict()
array = []

for i in range(num):
    name, state = input().split()
    if state == "enter":
        company[name] = 1
    else:
        company[name] = 0
    
for i in company.keys():
    if company[i] == 1:
        array.append(i)
        
array.sort(reverse = True)

for i in range(len(array)):
    print(array[i])
