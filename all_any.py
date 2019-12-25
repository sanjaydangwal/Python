l1=[2,4,6,8,10]
l2=[3,5,7,9,10]

evens = [i%2==0 for i in l2]
print(any(evens))