a=int(input('1:'))
b=int(input('2:'))
c=input('计算方式:')
if c=='a':
    print(a+b)
elif c=='b':
    print(a-b)
elif c=='c':
    print(a*b)
elif c=='d':
    print(a/b)
else:
    print('啥也不是')