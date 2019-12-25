def palindrom(string):
    return string == string[::-1]
string = input("enter a string  :   ")
if palindrom(string):
    print ("string is palindrom ")
else:
    print("string is not palindrom")