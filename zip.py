# l1 = [1,3,5,7,9]
# l2 = [2,4,6,8,10]
# l3 = []
# for pear in zip(l1,l2):
#     l3.append(max(pear))
# print(l3)

tuple_list = [(1,2),(3,4),(5,6),(7,8),(9,10)]
l1,l2 =(list(zip(*tuple_list)))
print(l1)
print(l2)

print(zip.__doc__)