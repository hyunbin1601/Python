# 분수 A/B는 분자가 A, 분모가 B인 분수를 의미한다. A와 B는 모두 자연수라고 하자.

# 두 분수의 합 또한 분수로 표현할 수 있다. 
# 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성하시오. 기약분수란 더 이상 약분되지 않는 분수를 의미한다.
# 두 분수의 합 또한 분수로 표현할 수 있다. 두 분수가 주어졌을 때, 그 합을 기약분수의 형태로 구하는 프로그램을 작성
# https://wikidocs.net/106676

from fractions import Fraction

num1, num2 = map(int, input().split())
num3, num4 = map(int, input().split())

frac1 = Fraction(num1, num2)
frac2 = Fraction(num3, num4)

frac3 = Fraction(frac1 + frac2)
print(frac3.numerator, end = ' ')
print(frac3.denominator)

