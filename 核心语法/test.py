class Car:
    def __init__(self,brand,name,price):
        self.brand=brand
        self.name=name
        self.price=price
    def running(self):
        print(f"{self.price},{self.name},{self.brand}")

    def __str__(self):
        return f"{self.price},{self.name},{self.brand}"

if __name__ == '__main__':
    c1=Car("BWM","X5",10000)
    print(c1)
    c2 = Car("BWM", "X5", 10000)
    print(c2)