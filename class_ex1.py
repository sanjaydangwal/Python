class laptop:
    discount = 21
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price
    def price_off(self):
        return  (self.price - (self.price*self.discount)/100)
o1 = laptop("dell","inspiron",100)
o1.discount = 40
print(o1.price_off())

