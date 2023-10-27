num1 = int(input())
num2 = int(input())

numArray = list(map(int, str(num2)))

print(num1 * numArray[2])  #3
print(num1 * numArray[1])  #4
print(num1 * numArray[0])  #5
print(num1 * num2)  #6    


