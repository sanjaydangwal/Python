total = 0
no = input("enter any number    :    ")
lenght = len(no)
while lenght > 0:
    total = total +int(no[lenght-1])
    lenght -=1
print(f"total of digits     :   {total}")