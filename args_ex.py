def power(num,*args):
    if args:
        return [i**num for i in args]
    else:
        print("you did't paas any value")
print(power(2,*(2,3,4,2,1,)))