class Person:
    count_object = 0
    def __init__(self,first_name,last_name,age):
        Person.count_object+=1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name+ " " +last_name
    @classmethod
    def count_obj(cls):
        return cls.count_object

o1 = Person("sanjay","dangwal",20)
o2 = Person("sanjay","dangwal",20)
o3 = Person("sanjay","dangwal",20)

print(Person.count_obj())