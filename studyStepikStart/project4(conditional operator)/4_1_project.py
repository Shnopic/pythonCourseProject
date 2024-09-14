#num = int(input())
#last_digit = num % 10    # последняя цифра числа
#first_digit = num // 10  # первая цифра числа
#if last_digit == first_digit:
#    print('ДА')
#else:
#    print('НЕТ')

#num1, num2, num3 = int(input()), int(input()), int(input())
#counter = 0  # переменная счётчик
#if num1 % 2 == 0:
#    counter = counter + 1  # увеличиваем счётчик на 1
#if num2 % 2 == 0:
#    counter = counter + 1  # увеличиваем счётчик на 1
#if num3 % 2 == 0:
#    counter = counter + 1  # увеличиваем счётчик на 1
#print(counter)

#password1=input()
#password2=input()
#if password1==password2 :
#    print('Пароль принят')
#else:
#    print('Пароль не принят')

#number=int(input())
#if number%2==0:
#    print('Четное')
#else:
#    print('Нечетное')

#number=int(input())
#d1=number//1000
#d2=number//100%10
#d3=number//10%10
#d4=number%10
#if d1+d4==d2-d3:
#    print('ДА')
#else:
#    print('НЕТ')

# d1=int(input())
# d2=int(input())
# d3=int(input())
# if d2-d1==d3-d2 and d2-d1!=0:
#     print('YES')
# else:
#     print('NO')

# m=int(input())
# n=int(input())
# if m-n>=0:
#     print(n)
# else:
#     print(m)

# m1=int(input())
# n2=int(input())
# d3=int(input())
# s4=int(input())
# if m1<=n2 and m1<=d3 and m1<=s4:
#     print(m1)
# elif n2<=m1 and n2<=d3 and n2<=s4:
#     print(n2)
# elif d3<=m1 and d3<=n2 and d3<=s4:
#     print(d3)
# else:
#     print(s4)

# m=int(input())
# if m>=0 and m<=13:
#     print('детство')
# elif m>13 and m<=24:
#     print('молодость')
# elif m>24 and m<=59:
#     print('зрелость')
# elif m>59:
#     print('старость')

a=int(input())
b=int(input())
c=int(input())
if a<0:
    a=0
if b<0:
    b=0
if c<0:
    c=0
print(a+b+c)
