def add_int(a,b):
    if(type(a)==int and type(b)==int):
        return a+b
    else:
        raise TypeError("you enterd string")

print(add_int('12',21))