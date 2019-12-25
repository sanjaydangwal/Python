def multiply(num,*args):
    num_list=list(args)
    for i in range(len(num_list)):
        num_list[i]=num_list[i]*num
    return tuple(num_list)
print(multiply(4,2,4,5,1,3))