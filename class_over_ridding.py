class Phone:
    discount_percent = 20
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self._price = max(0,price)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = new_price
    
    @property
    def complete_name(self):
        return f"{self.brand} {self.name}"
    
    def apply_discount(self):
        self._price -= (self.discount_percent*self._price)/100
class Smart_phone(Phone):
    def __init__(self,brand,name,price,ram,internal_storage,rear_camera):
        super().__init__(brand,name,price)
        self.ram = ram
        self.internal_storage = internal_storage
        self.rear_camera = rear_camera

class fleg_ship(Smart_phone):
    def __init__(self,brand,name,price,ram,internal_storage,rear_camera,front_camera):
        super().__init__(brand,name,price,ram,internal_storage,rear_camera)
        self.front_camera = front_camera

galaxy_s8 = fleg_ship("samsung","glaxy s8",45000,"4 gb","64 gb","13 mp","8 mp")

print(galaxy_s8.complete_name)
print(galaxy_s8.price)
galaxy_s8.apply_discount()
print(galaxy_s8.price)
galaxy_s8.discount_percent = 10
galaxy_s8.apply_discount()
print(galaxy_s8.price)
