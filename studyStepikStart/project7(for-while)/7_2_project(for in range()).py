# for i in range(100, 1000):  # перебираем числа от 100 до 999
#     if i % 10 == 7:         # используем остаток от деления на 10, для получения последней цифры
#         print(i)

# for i in range(56, 171, 2):
#     print(i)

# m,n=int(input()),int(input())
# for i in range (m,n+1):
#     print(i)

# m,n=int(input()),int(input())
# if m<n:
#     for i in range(m,n+1):
#         print(i)
# else:
#     for i in range(m,n-1,-1):
#         print(i)


# #вывод нечетных чисел при m>n
# m,n=int(input()),int(input())
# for i in range(m%2-1+m,n-1,-2):
#     print(i)


# m,n=int(input()),int(input())
# for i in range(m,n+1):
#     if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
#         print(i)


m=int(input())
for i in range(1,11):
    print(m, 'x', i, '=', m*i)