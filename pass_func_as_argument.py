li = [1,2,3,4,5,6,7,8]
def func(func,li):
    lis = []
    for num in li:
        lis.append(func(num))
    return lis

print(func(lambda num:num**2,li))