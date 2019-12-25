def add(*args):
    sum=0
    if all([type(arg)==int or type(arg)==float for arg in args]):
        for i in args:
            sum+=i
        print(f"sum :   {sum}")
    else:
        print("invalid input")
add(1,2,3,4,2,1,12)