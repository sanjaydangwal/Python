with open("file_ex.txt","r") as fr:
    with open("file_result.txt","w") as fw:
        for line in fr.readlines():
            name,salary = line.split(",")
            fw.write(f"{name}'s salary is {salary}")