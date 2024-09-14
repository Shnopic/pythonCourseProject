# # break continue else

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа
#
# if flag:  # эквивалентно if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')



# num = int(input())
# number = num
# flag = False
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     num //= 10
#
# if flag:  # эквивалентно if flag == True:
#     print('Число', number, 'содержит цифру 7')
# else:
#     print('Число', number, 'не содержит цифру 7')



# while True:
#     query = get_new_query() #  получаем новый запрос на обработку
#     query.process()         #  обрабатываем запрос



# while True:
#     if условие 1:  # условие для остановки цикла
#         break
#     ...
#     if условие 2:  # еще одно условие для остановки цикла
#         break
#     ...
#     if условие 3:  # еще одно условие для остановки цикла
#         break



# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)



# while условие:
#     блок кода1
# else:
#     блок кода2
#
# # или
#
# for i in range(10):
#     блок кода1
# else:
#     блок кода2



#Если слово else отсутствует в описании цикла, то блок кода2 будет выполняться после завершения цикла, /
# несмотря ни на что. Если же слово else присутствует, то блок кода2 будет выполняться только в том случае, /
# если цикл завершается штатным образом. Под штатным завершением цикла подразумевается его завершение /
# без использования оператора прерывания break.


# # Замена условия на else
# num = int(input())
# n = num
# flag = False
# while n != 0:
#     last = n % 10
#     if last == 7:
#         flag = True
#         break        # прерываем цикл, так как число гарантированно содержит цифру 7
#     n //= 10
#
# if flag == True:
#     print('Число', num, 'содержит цифру 7')
# else:
#     print('Число', num, 'не содержит цифру 7')
#
#
# num = int(input())
# n = num
# while n != 0:
#     last = n % 10
#     if last == 7:
#         print('Число', num, 'содержит цифру 7')
#         break
#     n //= 10
# else:
#     print('Число', num, 'не содержит цифру 7')



# #наименьший делитель
# n=int(input())
# for i in range(2,n+1):
#     if n%i==0:
#         print(i)
#         break


#правила
# n=int(input())
# for i in range(1,n+1):
#     if 5<=i<=9:
#         continue
#     if 17<=i<=37:
#         continue
#     if 78<=i<=87:
#         continue
#     print(i)