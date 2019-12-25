# def square(num):
#     return num**2
# num_list = [1,2,3,4,5,6,7]

# print(tuple(map(square,num_list)))

string_list =['abc','abcd','abcde']
print([len(name) for name in string_list])
lenght = []
for name in string_list:
    lenght.append(len(name))
print(lenght)

print(list(map(len,string_list)))

