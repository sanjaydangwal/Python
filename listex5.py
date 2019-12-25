def coman(l,m):
    coman_element = []
    for i in l:
        if i in m and not i in coman_element:
            coman_element.append(i)
    return coman_element
numbers,numbers2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],[2,4,6,8,10]
print(coman(numbers,numbers2))