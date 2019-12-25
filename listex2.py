def reverse(l):
    reverse_list =[]
    for i in range(len(l)):
        reverse_list.append(l.pop())
        #print(l)
    return reverse_list
name = input("enter a list  :   ").split(",")
#print(name)
for j in reverse(name):
    print(j, end =",")
