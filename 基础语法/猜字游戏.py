import random
if __name__ == '__main__':
    random_number=random.randint(1,100)

    while(True):
        a = int(input("你猜："))
        if(a==random_number):
            print("猜对啦")
            break
        else:
            print("猜错了，重新猜")
            continue