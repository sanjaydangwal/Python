f = open(r"D:\python cource\files\file1.txt")
print(f.read())

print(f.tell())
f.seek(0)
print(f.tell())
print(f.readlines())
f.seek(0)
for i in f:
    print(i,end="")