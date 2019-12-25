class Phone:
    discount_percentage = 10
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    @property
    def full_name(self):
        return f"{self.brand} {self.name}"
    def apply_discount(self):
        self.price -= (self.price*self.discount_percentage)//100
    def __str__(self):
        return f"{self.brand} {self.name}"
class SmartPhone(Phone):
    def __init__(self,brand,name,price,ram,camera):
        super().__init__(brand,name,price)
        self.ram = ram
        self.camera = camera
    
class MobileStore:
    def __init__(self):
        self.phone = []
        self.smartPhone = []
    def add_mobile(self,mobile):
        if(isinstance(mobile,Phone)):
            self.phone.append(mobile)
        elif(isinstance(mobile,SmartPhone)):
            self.smartPhone.append(mobile)
        else:
            raise TypeError("paas only object of phone or smartphone")

mob1= Phone("nokia","5233",3299)
mob2 = SmartPhone("samsung","galaxy s8",4300,"4 gb","13 mp")
print(mob2.full_name)
print(mob1.full_name)
mobostore = MobileStore()
mobostore.add_mobile(mob1)
mobostore.add_mobile(mob2)
print(mobostore.phone)
print(mobostore.smartPhone)
print(isinstance(mob2,SmartPhone))
