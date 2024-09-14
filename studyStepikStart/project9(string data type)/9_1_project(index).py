# s = 'Python'
# print(s[0])
# print(s[-6])

# s = 'abcdef'
# for i in range(len(s)):
#     print(s[i])

# s = 'abcdef'
# for c in s:
#     print(c)

# n=input()
# sum=0
# for i in range(len(n)):
#     sum += int(n[i])
# print(sum)

# #наличие цифр
# n=input()
# flag=False
# for i in range(10):
#     if str(i) in n:
#         flag=True
#         print('Цифра')
#         break
# if flag == False:
#     print('Цифр нет')

# n=input()
# sum1,sum2=0,0
# for i in range(len(n)):
#     if n[i]=='+':
#         sum1+=1
#     elif n[i]=='*':
#         sum2+=1
# print('Символ + встречается', sum1, 'раз')
# print('Символ * встречается', sum2, 'раз')

# n=input()
# sum=0
# for i in range(1,len(n)):
#     if n[i]==n[i-1]:
#         sum+=1
# print(sum)


# #подсчет гласных и согласных
# n=input()
# sum1,sum2=0,0
# for i in range(len(n)):
#     if str.lower(n[i]) in 'ауоыиэяюе':
#         sum1+=1
#         continue
#     elif str.lower(n[i]) in 'бвгджзйклмнпрстфхцчшщ':
#         sum2+=1
# print('Количество гласных букв равно', sum1)
# print('Количество согласных букв равно', sum2)


#перевод числа в двоичное
n=int(input())
s,r='',''
while n>0:
    digit=n%2
    s+=str(digit)
    n=n//2
for i in range(len(s)-1,-1,-1):
    r+=s[i]
print(r)