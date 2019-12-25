import math
def solve(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    return x1, x2
a,b,c = input("ENTER THE VALUE OF A, B AND C SEPRATE BY ',' ").split(",")

x1,x2 = solve(int(a),int(b),int(c))
print(f"value of x1 is {x1} and  x2 is {x2} ")