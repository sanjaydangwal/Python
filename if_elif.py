name = input("enter your name   :   ")
age = int(input("enter your age    :    "))
if age<=0 :
    print("you can't watch show.!!!")
elif 0<age<=9:
    print('ticket price      :     FREE')
elif 9<age<=20:
    print("ticket price      :     70")
elif 20<age<=30:
    print("ticket price      :     100")
elif 30<age<=50:
    print("ticket price      :     120")
elif 50<age<=65:
    print("ticket price      :     140")
else :
    print("ticket price      :     150")
