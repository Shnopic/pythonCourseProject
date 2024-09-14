# #обработка цифр в числе
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа
from itertools import count

# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')


# n=int(input())
# while n != 0:
#     last_d=n%10
#     print(last_d)
#     n=n//10


# n=int(input())
# while n != 0:
#     last_d=n%10
#     print(last_d, end='')
#     n=n//10


# #минимальная и максимальная цифры числа
# n=int(input())
# min_d=9
# max_d=0
# while n != 0:
#     digit=n%10
#     if min_d>digit:
#         min_d=digit
#     if max_d<digit:
#         max_d=digit
#     n=n//10
# print('Максимальная цифра равна', max_d)
# print('Минимальная цифра равна', min_d)


# #все вместе
# n=int(input())
# counter=0
# total_sum=0
# total_mult=1
# amount=len(str(n))
# f_l_sum=0
#
# while n != 0:
#     digit=n%10
#     total_sum += digit
#     counter += 1
#     total_mult *= digit
#     if counter == 1 or counter == amount:
#         f_l_sum += digit
#     n=n//10
#
# avg=total_sum/amount
# print(total_sum, amount, total_mult, avg, digit, f_l_sum, sep='\n')


# #вывод второй цифры в числе
# n=int(input())
# amount=len(str(n))
# counter=0
# while n != 0:
#     digit=n%10
#     counter+=1
#     if counter==amount-1:
#         print(digit)
#     n=n//10


# #все ли цифры одинаковые?
# n=int(input())
# flag=True
# counter=0
# while n != 0:
#     digit=n%10
#     if counter != 0 and digit != digit_previous:
#         flag = False
#     counter += 1
#     digit_previous=digit
#     n=n//10
# if flag==True:
#     print('YES')
# else:
#     print('NO')


#упорядоченные цифры
n=int(input())
flag=True
counter=0
while n != 0:
    digit=n%10
    if counter != 0 and digit < digit_previous:
        flag = False
    counter += 1
    digit_previous=digit
    n=n//10
if flag==True:
    print('YES')
else:
    print('NO')