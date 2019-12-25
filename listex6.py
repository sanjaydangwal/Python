def innerlist(l):
    no=0
    for i in l:
        if type(i)==list:
            no+=1
    return no
list_no = [1,2,3,[1,2,3,4,3],12,3,[3,42,12,]]
print(innerlist(list_no))
#print(type(list_no))