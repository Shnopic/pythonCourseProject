#print(10 // 3)  # округление в меньшую сторону
#print(-10 // 3)  # округление в меньшую сторону

#a = 15 // (16 % 7)
#b = 34 % a * 5 - 29 % 5 * 2
#print(a + b)

#b=int(input())
#q=int(input())
#n=int(input())
#print(b*q**(n-1))

#n=int(input())
#if n%2==0:
#    print(n//2)
#else:
#    print(n//2+1)

#n=int(input())
#print(n, 'мин - это', n//60, 'час', n%60, 'минут.')

#m=int(input())
#print((m-1)//4+1)

#number=int(input())
#d1=number//100
#d2=(number//10)%10
#d3=number%10
#print('Сумма цифр =', d1+d2+d3)
#print('Произведение цифр =', d1*d2*d3)

#number=int(input())
#d1=number//100
#d2=(number//10)%10
#d3=number%10
#print(d1, d2, d3, '\n', d1 , d3, d2, '\n', d2 , d1, d3, '\n', d2 , d3, d1,
#      '\n', d3 , d1, d2, '\n', d3 , d2, d1, sep='')


#number=int(input())
#d1=number//1000
#d2=(number//100)%10
#d3=(number//10)%10
#d4=number%10
#print('Цифра в позиции тысяч равна', d1)
#print('Цифра в позиции сотен равна', d2)
#print('Цифра в позиции десятков равна', d3)
#print('Цифра в позиции единиц равна', d4)

#a=int(input())
#b=int(input())
#print('Квадрат суммы', a, 'и', b, 'равен', (a+b)**2)
#print('Сумма квадратов', a, 'и', b, 'равна', a**2+b**2)

#a=int(input())
#b=int(input())
#c=int(input())
#d=int(input())
#print(a**b+c**d)

n=int(input())
print(n*3 + n*10*2 + n*100)