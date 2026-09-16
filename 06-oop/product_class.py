class Product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count+=1

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}.")

    @classmethod
    def get_count(cls):
        print(f"total products in store = {cls.count}")
    @staticmethod
    def cal_discount(price,discount):
        print(f"Final price is {price-(price * discount/ 100)}")



p1=Product("Phone",10_000)
p2=Product("laptop",50_000)
p2=Product("Book",1000)

p1.cal_discount(10000,12)
