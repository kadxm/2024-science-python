a='zhangsan'
b='202206'
for i in range(3):
    c=input('请输入账号:')
    d=input('请输入密码:')
    if a==c and b==d:
        print('登录成功')
        exit()
    else:
        print('登录失败')
print('登陆失败')