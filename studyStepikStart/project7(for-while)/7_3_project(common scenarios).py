# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
#
# print('Было введено', counter, 'чисел, больших 10.')


# #обмен переменных
# x, y = y, x


# #простое число
# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#
# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')


# #наибольшее число
# largest = 0
# for _ in range(10):
#     num = int(input())
#     if num > largest:
#         largest = num
#
# print('Наибольшее число равно', largest)


# #операторы присваивания
# x += 5	#x = x + 5
# x -= 2	#x = x - 2
# x *= 10	#x = x * 10
# x /= 4	#x = x / 4
# x //= 4	#x = x // 4
# x %= 4	#x = x % 4


# counter=0
# a,b=int(input()),int(input())
# for i in range(a,b+1):
#     if i**3%10==4 or i**3%10==9:
#         counter += 1
# print(counter)


# n=int(input())
# total=0
# for i in range(n):
#     x=int(input())
#     total += x
# print(total)


#Асимптотическое приближение
# import math
# n=int(input())
# total=0
# for i in range(1,n+1):
#     total += i**(-1)
# total -= math.log(n)
# print(total)


# n=int(input())
# total=0
# for i in range(1, n+1):
#     if i**2%10==2 or i**2%10==5 or i**2%10==8:
#         total += i
# print(total)


# import math
# n=int(input())
# print(math.factorial(n))


# total=1
# for i in range(10):
#     n=int(input())
#     if n != 0:
#         total *= n
# print(total)


# total=0
# n=int(input())
# for i in range (1,n+1):
#     if n%i==0:
#         total += i
# print(total)


# n=int(input())
# total=0
# for i in range (1,n+1):
#     total += (-1)**(i+1)*i
# print(total)


# #Получение наибольшего и второго наибольшего числа
# n=int(input())
# l1=0
# l2=0
# for i in range(1,n+1):
#     m=int(input())
#     if m>l1:
#         l2=l1
#         l1=m
#     if l2<m<l1:
#         l2=m
# print(l1, l2, sep='\n')


# #все числа четные
# flag=True
# for i in range(10):
#     n=int(input())
#     if n%2==1:
#         flag=False
# if flag==True:
#     print('YES')
# else:
#     print('NO')


#вывод n первых членов последовательности Фибоначчи
n1=1
n2=1
total=0
n=int(input())
for i in range(1,n+1):
    if i==1 or i==2:
        print('1', end=' ')
    else:
        total = n1+n2
        n1=n2
        n2=total
        print(total, end=' ')