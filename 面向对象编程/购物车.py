
class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num
    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"
    def updata_info(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num
        print("更新成功")

class Shop_sysdem:
    system_version=1
    system_name="购物车管理系统"
    goods_dict = {}

    def add_goods(self):
        name=input("please input name:")
        price=int(input("please input thr price:"))
        num=int(input("please input the num:"))
        self.goods_dict[name]={"price":price,"num":num}
        print("add the goods DONE")
    def delete_goods(self):
        name=input("please input the name for delete:")
        self.goods_dict.pop(name)
    def change_goods(self):
        name=input("please input the name for change:")
        price = int(input("please input the price:"))
        nums = int(input("please input the nums:"))
        self.goods_dict[name] = {"price": price, "nums": nums}
    def find_goods(self):
        for name,info in self.goods_dict.items():
            print(f"商品名称: {name}, 商品价格: {info['price']}, 商品数量: {info['nums']}")

def main():
    shop=Shop_sysdem
    menu = """
       ===== 购物车管理系统 =====
       1. 添加商品
       2. 删除商品
       3. 修改商品
       4. 查询商品
       5. 显示所有商品
       0. 退出系统
       ==========================
       """
    while True:
        print(menu)
        choice=input("please input:")
        if choice=="1":
            shop.add_goods()
        elif choice=="2":
            shop.delete_goods()
        elif choice=="3":
            shop.change_goods()
        elif choice=="4":
            shop.find_goods()
        elif choice=="0":
            print("Thank you for use")
            break
        else:
            print("fail input")

if __name__=="__main__":
    main()


