class phone:
    def __init__(self ,name,model,price):
        self.name = name
        self.model = model
        self._price = max(0,price)
    @property
    def complete_specification(self):
        return f"{self.name + self.model} price {self.price}"
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        self._price = max(0,new_price)

class smartphone(phone):
    def __init__(self,name,model,price,ram,storage,rear_camera):
        #phone.__init__(self,name,model,price)
        super().__init__(name,model,price)
        self.ram = ram
        self.storage = storage
        self.rear_camera = rear_camera
m1 = phone("samsung","guru",3000)
print(m1.price)
m2 = smartphone("samsung","galaxy j7 prime",13000,"3 gb","32 gb","13 mp")
print(m2.complete_specification)
print(m2.rear_camera)
print(m2)
print(m2.__dict__)
