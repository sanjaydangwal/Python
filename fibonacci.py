def fibonacci_seq(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (fibonacci_seq(n-2)+fibonacci_seq(n-1))
num = int(input("enter any number   :   "))
print(f"fibonacci series for {num} number.")
for i in range(1,num+1):
    print(fibonacci_seq(i), end = ", ")