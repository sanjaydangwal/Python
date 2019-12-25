def reverse_list(l):
    l_list = []
    for i in  l:
        l_list.append(i[::-1])
    return l_list

name = input("enter your name    :   ").split(",")
print(reverse_list(name))