num1, num2, num3 = map(int, input().split())


result1 = (num1+num2)%num3
result2 = ((num1%num3)+(num2%num3))%num3
result3 = (num1*num2)%num3
result4 = ((num1%num3)*(num2%num3))%num3

print(result1)
print(result2)
print(result3)
print(result4)