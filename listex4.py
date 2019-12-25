def odd_even(l):
    odd = []
    even = []
    for i in l:
        if i%2==1:
            odd.append(i)
        else:
            even.append(i)
    odd_even_list=[]
    odd_even_list.append(odd)
    odd_even_list.append(even)
    return odd_even_list
new_list = input("enter a list  : ").split(",")
for i in range(len(new_list)):
    new_list[i] = int(new_list[i])
print(odd_even(new_list))
input()
