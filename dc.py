square = {f"square of {num}":num**2 for num in range(1,11)}
for key,value in square.items():
    print(f"{key}:{value}")

string = 'sanjay'
word_counter = {char:string.count(char) for char in string}
for key,value in word_counter.items():
    print(f"{key}:{value}")