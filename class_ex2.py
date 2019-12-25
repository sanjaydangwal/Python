class Person:
    count_obj = 0
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.count_obj +=1

obj = Person("sanjay","dangwal",19)
obj1 = Person("vijay","dsfs",88)
print(Person.count_obj)
