import sys

number = list(map(int, sys.stdin.readline().split()))

print(number[0] + number[1])
print(number[0] - number[1])
print(number[0] * number[1])
print(int(number[0] / number[1]))
print(number[0] % number[1])
