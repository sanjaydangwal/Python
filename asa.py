def func(string):
    temp = ""
    for i in range(len(string)):
        if i%2==0:
            temp+=string[i].upper()
        else:
            temp+=string[i].lower()
    return temp
print(func("hello"))
