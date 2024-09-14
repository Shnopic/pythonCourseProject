# a = 13
# b = 7
#
# total = a + b
# diff = a - b
# prod = a * b
# div1 = a / b
# div2 = a // b
# mod = a % b
# exp = a ** b
#
# print(a, '+', b, '=', total)
# print(a, '-', b, '=', diff)
# print(a, '*', b, '=', prod)
# print(a, '/', b, '=', div1)
# print(a, '//', b, '=', div2)
# print(a, '%', b, '=', mod)
# print(a, '**', b, '=', exp)


# num1 = 25_000_000
# num2 = 25000000
# print(num1)
# print(num2)


# num = float(input())

# #площадь треугольника
# a=float(input())
# b=float(input())
# print(a*b/2)


# #старушки, идущие на встречу
# S=float(input())
# V1=float(input())
# V2=float(input())
# print(S/(V1+V2))


# #обратное число
# a=float(input())
# if a==0:
#     print('Обратного числа не существует')
# else:
#     print(a**(-1))


# #перевод фаренгейтов в цельсий
# tf=float(input())
# print((tf-32)*5/9)


# #dog age
# age=int(input())
# if 0<=age<=2:
#     print(10.5*age)
# else:
#     print((10.5*2)+(age-2)*4)


# #.x
# n=float(input())
# print((int(n*10))%10)


# #дробная часть
# n=float(input())
# print(n-int(n))


# a,b,c,d,e=int(input()),int(input()),int(input()),int(input()),int(input())
# print('Наименьшее число =', min(a,b,c,d,e))
# print('Наибольшее число =', max(a,b,c,d,e))

# #сортировка трех
# a,b,c=int(input()),int(input()),int(input())
# if max(a,b,c)==c:
#     print(c, max(a, b), min(a, b), sep='\n')
# elif max(a,b,c)==b:
#     print(b, max(a, c), min(a, c), sep='\n')
# else:
#     print(a, max(c, b), min(c, b), sep='\n')


# #интересное число
# num=int(input())
# d1=num//100
# d2=num//10%10
# d3=num%10
# if max(d1,d2,d3)-min(d1,d2,d3)==(d1+d2+d3)-max(d1,d2,d3)-min(d1,d2,d3):
#     print('Число интересное')
# else:
#     print('Число неинтересное')


# a,b,c,d,e=abs(float(input())),abs(float(input())),abs(float(input())),abs(float(input())),abs(float(input()))
# print(a+b+c+d+e)


#манхэттенское расстояние
p1,p2,q1,q2=int(input()),int(input()),int(input()),int(input())
print(abs(p1-q1)+abs(p2-q2))