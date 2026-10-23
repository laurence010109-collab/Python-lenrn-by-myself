# 需求：小智的银行卡中有10000元，现在到ATM进行取钱操作，
# 请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额。
if __name__ == '__main__':
    money=10000
    mina=int(input("请输入取款密码："))

    if(mina==123456):
        qukian_money = int(input("密码正确，请输入取款金额："))
        if(qukian_money<=money):
            print("取款成功，剩余%d"%(money-qukian_money))
            print(f"取款成功，剩余{money - qukian_money}")
        else:
            print("余额不足")
    else:
        print("密码错误")