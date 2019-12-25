with open(r"files\write.txt","r+") as f:
    f.seek(len(f.read()))
    f.write('sanjay \n')
