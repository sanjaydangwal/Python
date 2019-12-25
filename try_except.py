while 1:
    try:
        age = int(input("enter your age   :   "))
        break
    except TypeError:
        print("invalid input")
    except:
        print("unexpected error")

if age < 18:
    print("you can't play game")
else:
    print("you can play game")