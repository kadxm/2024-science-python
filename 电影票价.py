a=0
while a!='退出':
    a=int(input('age:'))
    if a<3:
        print(0)
    elif a<13:
        print(20)
    elif a=='退出':
        break
    else:
        print(40)