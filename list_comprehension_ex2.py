def change(l):
    return  [str(i) for i in l if (type(i)==int or type(i)==float)]
input_list = ["sanjay",1,4,2,1.3,23.3,(1,2,3),["sanjay","sagar"]]
print(change(input_list))