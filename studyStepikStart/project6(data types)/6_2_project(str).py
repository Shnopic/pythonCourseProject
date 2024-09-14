# s1 = 'abcdef'
# length1 = len(s1)               # считаем длину строки из переменной s1
# length2 = len('Python rocks!')  # считаем длину строкового литерала
# print(length1)
# print(length2)


# team=input()
# print('Футбольная команда ' + team + ' имеет длину ' + str(len(team)) + ' символов')


# a,b,c=input(),input(),input()
# if min(len(a),len(b),len(c)) == len(a):
#     print(a)
# elif min(len(a),len(b),len(c)) == len(b):
#     print(b)
# elif min(len(a),len(b),len(c)) == len(c):
#     print(c)
# if max(len(a),len(b),len(c)) == len(a):
#     print(a)
# elif max(len(a), len(b), len(c)) == len(b):
#     print(b)
# elif max(len(a), len(b), len(c)) == len(c):
#     print(c)


# проверка возможности арифметической прогрессии
# a,b,c=input(),input(),input()
# a1,b1,c1=len(a),len(b),len(c)
# d=(max(a1,b1,c1)-min(a1,b1,c1))/2
# if (a1+b1+c1)-max(a1,b1,c1)-min(a1,b1,c1) == min(a1,b1,c1) + d:
#     print('YES')
# else:
#     print('NO')


#оператор in
# s = 'https://pygen.ru/'
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')

# if len(s) == 1 and s in 'aeiou':
#     print('YES')

# s = 'Sigma'
# print('a' in s)
# print('z' in s)


# s=input()
# if 'синий' in s:
#     print('YES')
# else:
#     print('NO')


# s=input()
# if 'суббота' in s or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')


s=input()
if '@' in s and '.' in s:
    print('YES')
else:
    print('NO')