#Цикл for (counting loops) and while (conditional loops)

# for i in range(10):
#     print('Python is awesome!')

# string=input()
# x=int(input())
# for i in range(x):
#     print(string)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# for i in range(int(input())):
#     print('*'*19)

# string=input()
# for i in range(10):
#     print(i, string)

# n=int(input())
# for i in range(n+1):
#     print('Квадрат числа', i, 'равен', i**2)

# n=int(input())
# for i in range(n):
#     print('*'*(n-i))

m=float(input())
p=float(input())/100
n=int(input())
for i in range(n):
    print(i+1, m)
    m=m+m*p
