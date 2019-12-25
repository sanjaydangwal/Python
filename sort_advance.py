user = [
    {'name':'sanjay','age':20,'score':324},
    {'name':'sagar','age':21,'score':322},
    {'name':'vijay','age':23,'score':364},
]

print(sorted(user,key=lambda info : info.get('score')))