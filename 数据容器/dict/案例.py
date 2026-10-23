if __name__ == '__main__':
    shopping_car={}
    while True:
        print("\n" + "=" * 30)
        print("欢迎使用购物车管理系统")
        print("1. 添加购物车")
        print("2. 修改购物车")
        print("3. 删除购物车")
        print("4. 查询购物车")
        print("5. 退出购物车")
        print("=" * 30)

        choice = input("请输入您的操作选项 (1-5)：")
        if choice=="1":
            name=input("please input the name:")
            price=int(input("please input the price:"))
            nums=int(input("please input the nums:"))
            shopping_car[name]={"price":price,"nums":nums}
        print(shopping_car)
        if choice == "2":
            name = input("please input the name for exchange:")
            price = int(input("please input the price:"))
            nums = int(input("please input the nums:"))
            shopping_car[name] = {"price": price, "nums": nums}
        if choice == "3":
            name = input("please input the name for delete:")
            shopping_car.pop(name)
        if choice == "4":
            for name, information in shopping_car.items():
                print(f"商品名称: {name}, 商品价格: {information['price']}, 商品数量: {information['nums']}")
        if choice == "5":
            break
        else:
            print("fail input")