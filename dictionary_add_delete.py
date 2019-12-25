user_info = {
    'name' : "sanjay" ,
    'age' : 19 ,
    'language' : "c,c++,html,css"
}

user_info['college']= "oimt"
print(user_info)
#poped_item=user_info.pop('age')
#print(poped_item)
poped_item = user_info.popitem()
print(user_info)
print(poped_item)