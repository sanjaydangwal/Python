def greater(num1,num2):
    if num1>num2:
        return num1
    return num2

a,b,c = input("enter three numbers saprate by ,     :   ").split(",")
print(f"largest number  :   {greater(greater(a,b),c)}")