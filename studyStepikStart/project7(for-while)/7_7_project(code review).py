#Производительность кода

# #составное ли число
# # #у любого составного числа есть делитель (отличный от 1), не превосходящий квадратного корня из числа
# num = int(input())
# flag = True
#
# for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#         flag = False
#         break
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')



# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# mx = -1000000
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > mx:
#             mx = x
# if s<0:
#     print(s)
#     print(mx)
# else:
#     print('NO')


# s = 0
# for i in range(1, 8):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# print(s)


# n = int(input())
# max_digit = -1
# while n != 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)


# #вывод старшей цифры (первой)
# n = int(input())
# while n > 9:
#     n = n // 10
# print(n)


n = int(input())
product = 1
while n != 0:
    digit = n % 10
    product = product * digit
    n = n // 10
print(product)