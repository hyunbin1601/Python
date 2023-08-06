# n = int(input())

# a = n / 5
# # b = n % 5
# c = n / 3
# # d = n % 3

# num = 0
# num1 = 0
# d = 0

# while True:
#     if n % 5 == 0:
#         print(int(n/5))
#         break
#     elif n % 3 == 0:
#         d = int(n/3)
#     if n % 5 != 0:
#         while True:
#             if n <= 2:
#                 if num > 0 and num1 > 0:
#                     print(min(d, num + num1))
#                     break
#                 else:
#                     print(-1)
#                     break
#             else:
#                 if n - 5 >= 0:
#                     num += 1
#                     if n-3 >= 0 and n-5 < 0:
#                         num1 += 1
#                         n = n-3
#                     else:
#                         n = n -5
                    
#         break