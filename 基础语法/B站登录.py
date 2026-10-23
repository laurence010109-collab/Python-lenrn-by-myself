import sys
if __name__ == '__main__':
    zhanghao=int(input("请输入账号："))
    mima=int(input("请输入密码："))
    if(zhanghao==18153377445 and mima==123456):
        print("登录成功")
    elif(zhanghao==123 and mima==123):
        print("登录成功")
    elif (zhanghao == 456 and mima == 456):
        print("登录成功")
    else: print("登录失败")