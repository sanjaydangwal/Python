def power_of_num(x):
    def power(n):
        return n**x
    return power

squre = power_of_num(3)
print(squre(2))