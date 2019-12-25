class student:
    def __init__(self,first_name,last_name,age):
        self.name = first_name +" " +last_name
        self.age = age

s1 = student("sanjay","dangwal",19)
print(s1.name)