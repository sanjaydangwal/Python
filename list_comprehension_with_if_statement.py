numbers = list(range(1,11))
even_num = [i for i in numbers if i%2==0]
odd_num = [i for i in range(1,11) if i%2!=0]
print(odd_num)
print(even_num)