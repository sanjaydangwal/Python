name,charcter = input("enter your name and a charcter    ").split(",")
print(f"lenght of name   :  {len(name.strip())}")
print(f"no or charcters in name     :   {name.lower().count(charcter.strip().lower())}")