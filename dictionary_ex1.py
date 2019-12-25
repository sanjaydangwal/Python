def squar_dict(n):
    squar = {}
    for i in range(1,n+1): 
        squar[i] = i**2
    return squar
n = int(input("enter any number :   "))
print(squar_dict(n))