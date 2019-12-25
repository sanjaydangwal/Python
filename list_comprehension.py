square = []
for i in range(1,11):
    square.append(i**2)
print(square)
square2 = [i**2 for i in range(1,11)]
print(square2)

negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)

negative2 = [-i for i in range(1,11)]
print(negative2)

names = ["sanjay","deepak","riya"]
first_latter = []
for name in names:
    first_latter.append(name[0])
print(first_latter)

first_latter2 = [name[0] for name in names]
print(first_latter2)