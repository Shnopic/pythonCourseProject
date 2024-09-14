# # Вложенные циклы

# for i in range(8):
#     for j in range(6):
#         print('*', end='')
#     print()

# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)



# n=int(input())
# for i in range(n):
#     for j in range (3):
#         print(n, end=' ')
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range (5):
#         print(i, end=' ')
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range (1,10):
#         print(i, '+', j, '=', i+j)
#     print()


#полная поебень
# n=int(input())
# for i in range (1,n+1):
#     for i in range(1,n//2+2):
#         print('*'*i)
#     for i in range(n//2+1,n):
#         print('*'*(n-i))
#     break

#нормальное решение
# n = int(input())
# for i in range(n):
#     k = (n // 2 + 1) - abs(n // 2 - i)
#     for _ in range(k):
#         print('*', end='')
#     print()


# n=int(input())
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end='')
#     print()



#
# Решение уравнений через вложенный цикл
#
# #Найдите все пары натуральных чисел (и их количество), являющихся решением уравнения 12x+13y=777
# total = 0
# for x in range(1, 65):
#     for y in range(1, 60):
#         if 12 * x + 13 * y == 777:
#             total += 1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)

# #Найдите все тройки натуральных чисел (и их количество), являющихся решением уравнения /
# # x^2+y^2+z^2=2020.
# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)


# for n in range(1,(365//28+1)):
#     for k in range(1,(365//30+1)):
#         for m in range(1,(365//31+1)):
#             if 28*n+30*k+31*m==365:
#                 print (n,k,m)


# for b in range(1,(100//10+1)):
#     for k in range(1,(100//5+1)):
#         for t in range(1,(100*2+1)):
#             if 10*b+5*k+0.5*t==100 and b+k+t==100:
#                 print (b,k,t)



#Опровержение Эйлера по Ферма
# #Полная поебень
# for a in range(1,151):
#     for b in range(1,151):
#         for c in range(1,151):
#             for d in range(1,151):
#                 for e in range(1,151):
#                     if a**5+b**5+c**5+d**5==e**5:
#                         print(a,b,c,d,e,a+b+c+d+e)
#                         break

#умное с комбинаторикой
# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(sum**(1/5))
#                 if sum==e**5:
#                     print(a, b, c, d, e, a + b + c + d + e)
#                     break




# n=int(input())
# m=0
# for i in range (1,n+1):
#     for j in range(i):
#         m += 1
#         print(m, end=' ')
#     print()

# #числовой треугольник
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,i*2):
#         if j<=i:
#             print(j,end='')
#         elif j>i:
#             print(i*2-j,end='')
#     print()
#
# #альтернатива
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 2 * i):
#         print(min(j, 2 * i - j), end='')
#     print()


# #число с максимальной суммой делителей
# a,b=int(input()),int(input())
# max_number=0
# total=0
# total_max=0
# for i in range(a,b+1):
#     for j in range(1,int(i**0.5)+1):
#         if i%j==0:
#             k=i/j
#             total += k
#             if k!=j:
#                 total += j
#     if total>=total_max:
#         max_number=i
#         total_max=total
#         total=0
#     else:
#         total=0
# print(max_number, int(total_max))


# #+ - это делитель
# n=int(input())
# for i in range(1,n+1):
#     print(i,end='')
#     for j in range(1,i+1):
#         if i%j==0:
#             print('+',end='')
#     print()


# #цифровой корень
# n=int(input())
# while n>9:
#     k = n
#     sum = 0
#     while k!=0:
#         sum += k%10
#         k=k//10
#     n=sum
# print(n)


# #сумма факториалов
# import math
# n=int(input())
# sum=0
# for i in range(1,n+1):
#     sum += math.factorial(i)
# print(sum)


# #простые числа
# a,b=int(input()),int(input())
# for i in range(a,b+1):
#     for j in range(2, int(i ** 0.5) + 1):
#         if i%j==0:
#             break
#     else:
#         if i!=1:
#             print(i)


# for a in range(1, 100):
#     for c in range(a+1, 100):
#         for d in range(c+1, 100):
#             for b in range(d+1,100):
#                 if a ** 3 + b ** 3 == c**3 + d ** 3:
#                     print(a, b, c, d, a ** 3 + b ** 3)


# n=int(input())
# for i in range(1,n+1):
#     if i==1 or i==n:
#         print('*'*19)
#     else:
#         print('*',' '*15,'*')


# n=int(input())
# while n>99:
#     k=n%10
#     n=n//10
# print(k)


n=int(input())
count_3,count_x,count_even,sum_more_5,mult,count_05=0,0,0,0,1,0
x=n%10
while n!=0:
    k=n%10
    if k==3: count_3 += 1
    if k==x: count_x += 1
    if k%2==0: count_even += 1
    if k>5: sum_more_5 += k
    if k>7: mult *= k
    if k==0 or k==5: count_05 += 1
    n=n//10
print(count_3,count_x,count_even,sum_more_5,mult,count_05,sep='\n')

