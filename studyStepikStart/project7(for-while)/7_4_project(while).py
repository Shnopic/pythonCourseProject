## Цикл while

# text = input()
# total = 0
# while text != 'stop':
#     total += int(text)
#     text = input()
#
# print('Сумма чисел равна', total)


# n=input()
# while n != 'КОНЕЦ':
#     print(n)
#     n=input()

# n=input()
# while n != 'КОНЕЦ' and n != 'конец':
#     print(n)
#     n=input()

# n=input()
# counter=0
# while n != 'стоп' and n != 'хватит' and n != 'достаточно':
#     counter += 1
#     n=input()
# print(counter)

# n=int(input())
# while n % 7 == 0:
#     print(n)
#     n=int(input())

# n=int(input())
# total=0
# while n >= 0:
#     total += n
#     n=int(input())
# print(total)

# n=int(input())
# counter=0
# while 0<n<=5:
#     if n == 5:
#         counter += 1
#     n=int(input())
# print(counter)


#подсчет наименьшего количества монет
n=int(input())
counter=0
while n!=0:
    if n>=25:
        n -= 25
        counter += 1
    elif n>=10:
        n -= 10
        counter += 1
    elif n>=5:
        n -= 5
        counter += 1
    else:
        n -= 1
        counter += 1
print(counter)