# n,k=int(input()),int(input())
# if n>k:
#     print('NO')
# elif n<k:
#     print('YES')
# else:
#     print("Don't know")

# a,b,c=int(input()),int(input()),int(input())
# if a==b==c:
#     print('Равносторонний')
# elif a!=b and b!=c and a!=c:
#     print('Разносторонний')
# else:
#     print('Равнобедренный')

# a,b,c=int(input()),int(input()),int(input())
# if a<=b<=c or c<=b<=a:
#     print(b)
# elif b<=a<=c or c<=a<=b:
#     print(a)
# elif a<=c<=b or b<=c<=a:
#     print(c)

# month=int(input())
# if month==2:
#     print(28)
# elif (month<=7 and month%2==1) or (month>=8 and month%2==0):
#     print(31)
# else:
#     print(30)

# weight=int(input())
# if weight<60:
#     print('Легкий вес')
# elif 60<=weight<64:
#     print('Первый полусредний вес')
# elif 64<=weight<69:
#     print('Полусредний вес')

# a,b,c=int(input()),int(input()),input()
# if c=='+' or c=='-' or c=='*' or c=='/':
#     if c=='+':
#         print(a+b)
#     elif c=='-':
#         print(a-b)
#     elif c=='*':
#         print(a*b)
#     elif c=='/':
#         if b==0:
#             print('На ноль делить нельзя!')
#         else:
#             print(a/b)
# else:
#     print('Неверная операция')

# red,blue,yellow='красный','синий','желтый'
# color1=input()
# color2=input()
# if (color1!=red and color1!=blue and color1!=yellow) or (color2!=red and color2!=blue and color2!=yellow):
#     print('ошибка цвета')
# elif color2==color1:
#     print(color2)
# elif (color1==red and color2==blue) or (color2==red and color1==blue):
#     print('фиолетовый')
# elif (color1==red and color2==yellow) or (color2==red and color1==yellow):
#     print('оранжевый')
# elif (color1==blue and color2==yellow) or (color2==blue and color1==yellow):
#     print('зеленый')

# num=int(input())
# if num==0:
#     print('зеленый')
# elif num<0 or num>=37:
#     print('ошибка ввода')
# elif 1<=num<=10:
#         if num%2==0:
#             print('черный')
#         else:
#             print('красный')
# elif 11<=num<=18:
#         if num%2==1:
#             print('черный')
#         else:
#             print('красный')
# elif 19<=num<=28:
#         if num%2==0:
#             print('черный')
#         else:
#             print('красный')
# elif 29<=num<=36:
#         if num%2==1:
#             print('черный')
#         else:
#             print('красный')

# a1,b1,a2,b2=int(input()),int(input()),int(input()),int(input())
# if b2<a1 or a2>b1:
#     print('пустое множество')
# elif b2==a1 or a2==b1:
#     if b2==a1:
#         print(b2)
#     else:
#         print(a2)
# elif a2 <= a1 and b2 <= b1:
#     print(a1,b2)
# elif a2 <= a1 and b2 >= b1:
#     print(a1,b1)
# elif a1<=a2<=b1 and b2 >= b1:
#     print(a2, b1)
# elif a1<=a2<=b1 and b2 <= b1:
#     print(a2, b2)

# a1,a2,b1,b2=int(input()),int(input()),int(input()),int(input())
# if (a1 % 2 == 0 and a2 % 2 == 0 and b1 % 2 == 0 and b2 % 2 == 0) or (a1 % 2 == 1 and b1 % 2 == 1 and a2 % 2 == 0 and b2 % 2 == 0) or (a1 % 2 == 0 and b1 % 2 == 0 and a2 % 2 == 1 and b2 % 2 == 1) or (a1 % 2 == 1 and a2 % 2 == 1 and b1 % 2 == 1 and b2 % 2 == 1) or (a1 % 2 == 0 and a2 % 2 == 1 and b1 % 2 == 1 and b2 % 2 == 0) or (a1 % 2 == 1 and a2 % 2 == 0 and b1 % 2 == 0 and b2 % 2 == 1) or (a1 % 2 == 1 and a2 % 2 == 0 and b1 % 2 == 1 and b2 % 2 == 0) or (a1 % 2 == 0 and a2 % 2 == 1 and b1 % 2 == 0 and b2 % 2 == 1) or (a1 % 2 == 0 and a2 % 2 == 0 and b1 % 2 == 1 and b2 % 2 == 1) or (a1 % 2 == 1 and a2 % 2 == 1 and b1 % 2 == 0 and b2 % 2 == 0):
#     print('YES')
# else:
#     print('NO')

# age=int(input())
# sex=input()
# if 10<=age<=15 and sex=='f':
#     print('YES')
# else:
#     print('NO')

# num=int(input())
# if num<1 or num>10:
#     print('ошибка')
# elif 1<=num<=3:
#     print(num*'I')
# elif num==4:
#     print('IV')
# elif num==5:
#     print('V')
# elif 6<=num<=8:
#     print('V',(num-5)*'I',sep='')
# elif num==9:
#     print('IX')
# elif num==10:
#     print('X')

# num=int(input())
# if num%2==1:
#     print('YES')
# elif 2<=num<=5 or num>20:
#     print('NO')
# elif 6<=num<=20 and num%2==0:
#     print('YES')

# a1,a2,b1,b2=int(input()),int(input()),int(input()),int(input())
# if (1<=a1<=8 and 1<=a2<=8 and 1<=b1<=8 and 1<=b2<=8) and ((b1-a1==b2-a2 or b1-a1==-(b2-a2))):
#     print('YES')
# else:
#     print('NO')

# a1,a2,b1,b2=int(input()),int(input()),int(input()),int(input())
# if (1<=a1<=8 and 1<=a2<=8 and 1<=b1<=8 and 1<=b2<=8) and ((b1-a1==b2-a2 or b1-a1==-(b2-a2) or a1==b1 or a2==b2)):
#     print('YES')
# else:
#     print('NO')


a1,a2,b1,b2=int(input()),int(input()),int(input()),int(input())
if (1<=a1<=8 and 1<=a2<=8 and 1<=b1<=8 and 1<=b2<=8) and ((abs(b1-a1)==2 and abs(b2-a2)==1) or (abs(b1-a1)==1 and abs(b2-a2)==2)):
    print('YES')
else:
    print('NO')
