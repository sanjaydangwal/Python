odd_even = {num:(f"{num*2}" if num%2==0 else f"{-num}") for num in range(1,11)}
print(odd_even)