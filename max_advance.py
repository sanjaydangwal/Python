names = ['sanjay','deepak bhatt','sagar']
print(max(names, key = lambda name:len(name)))

user_info = [
    {'name':'sanjay','score':308,'age':20},
    {'name':'vijay','score':104,'age':25},
    {'name':'deepak','score':503,'age':23}
]

user_info2 = {
    'sanjay':{'score':308,'age':20},
    'vijay':{'score':104,'age':25},
    'deepak':{'score':503,'age':23}
}

print(max(user_info,key = lambda info:info.get('score')).get('name'))
print(min(user_info,key=lambda info:info.get('age')))