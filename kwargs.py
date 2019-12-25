def kwargs_exampel(**kwargs):
    for k,v in kwargs.items():
        print(f"{k} : {v}")

kwargs_exampel(name='sanjay',age=19)

user_info = {
    'name' : 'sanjay dangwal',
    'age' : 19
}

kwargs_exampel(**user_info)