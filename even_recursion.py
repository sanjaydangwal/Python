def print_even(n):
    if(n>0):
        print_even(n-1)
        if(n%2==0):
            print(n,end = " ,")
        
n = int(input("enter a number   "))
print_even(n)