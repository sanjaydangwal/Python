name = input("enter your name   :    ")
age = int(input("enter your age  :  "))
if (name.strip()[0]=='a' or name.strip()[0]=='A') and age >= 14 :
    print("you can watch coco.   ")
else:
    print("you can't watch moive.   ")