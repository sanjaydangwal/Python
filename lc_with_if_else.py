def fun(l):
    new_list = []
    for i in l:
        if i%2==0:
            new_list.append(i*2)
        else:
            new_list.append(-i)
    return new_list

numbers = list(range(1,11))
print(fun(numbers))

new_list2 = [i*2 if i%2==0 else -1 for i in numbers]
print(new_list2)