def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("please dont't divide with zero")
    except TypeError:
        print("please input only numbers")

print(divide(4,2))
print(divide(23,0))
print(divide(32,'23'))