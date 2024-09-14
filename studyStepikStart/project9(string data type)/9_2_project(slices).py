# s = 'abcdefghij'
# print(s[2:5])
#print(s[2:])
#print(s[1:7:2])
#print(s[::-1])    #обратный порядок

#изменение символа строки
#s = s[:4] + 'X' + s[5:]


# #палиндром
# s=input()
# s1=s[::-1]
# if s==s1:
#     print('YES')
# else:
#     print('NO')


# s=input()
# print(len(s), s*3, s[0], s[:3], s[-3:], s[::-1], s[1:len(s)-1], sep='\n')


# s=input()
# print(s[2], s[-2], s[:5], s[:len(s)-2], s[::2], s[1::2], s[::-1], s[::-2], sep='\n')


s=input()
if len(s)%2==0:
    print(s[(len(s)//2):], s[:len(s)//2], sep='')
else:
    print(s[len(s)//2+1:], s[:len(s)//2+1], sep='')