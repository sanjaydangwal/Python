def squer_list(l):
    squ_list = []
    for i in l:
        squ_list.append(i**2)
    return squ_list

numbers = input("enter numbers  :   ").split(",")
for j in range(len(numbers)):
    numbers[j]=int(numbers[j])
print(squer_list(numbers))




