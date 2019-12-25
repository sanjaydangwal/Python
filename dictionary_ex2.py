user_info = {}
user_info['name'] = input("enter your name  :   ")
user_info['age'] = input("enter your age     :   ")
user_info['fav_movie'] = input("enter your favorite movies separate by ','    :   ").split(",")
user_info['fav_subject'] = input("enter your favorite subject seprate by ','    :   ").split(",")

for key,value in user_info.items():
    print(f"{key}   :   {value}")