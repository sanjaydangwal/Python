def even_num(n):
    for i in range(n+1):
        if(i%2==0):
            yield i
        
for i in even_num(10):
    print(i)