# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0:
#     print('1 четверть')
# if x < 0 and y > 0:
#     print('2 четверть')
# if x < 0 and y < 0:
#     print('3 четверть')
# if x > 0 and y < 0:
#     print('4 четверть')

# n=int(input())
# if -1<n<17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n=int(input())
# if n<=(-3) or n>=7:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n=int(input())
# if (-30)<n<=(-2) or 7<n<=25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')

# n=int(input())
# if 1000<=n<=9999 and (n%7==0 or n%17==0):
#     print('YES')
# else:
#     print('NO')

# n1=int(input())
# n2=int(input())
# n3=int(input())
# if (n1+n2)>n3 and (n1+n3)>n2 and (n2+n3)>n1:
#     print('YES')
# else:
#     print('NO')

# year=int(input())
# if (year%4==0 and year%100!=0) or year%400==0:
#     print('YES')
# else:
#     print('NO')

# p11=int(input())
# p12=int(input())
# p21=int(input())
# p22=int(input())
# if p11==p21 or p12==p22:
#     print('YES')
# else:
#     print('NO')

p11=int(input())
p12=int(input())
p21=int(input())
p22=int(input())
if (-1<=p21-p11<=1) and (-1<=p22-p12<=1):
    print('YES')
else:
    print('NO')