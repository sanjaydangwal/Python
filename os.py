import os
os.chdir(r"d:\python cource\files")
# if(os.path.exists("data")):
#     print("already exist")
# else:
#     os.mkdir("data")
for files in os.listdir():
    path = os.path.join(os.getcwd(),files)
    print(path)