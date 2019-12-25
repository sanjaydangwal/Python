roll_no = [1,2,3,4]
maths = [100,90,80,70]
science = [90,70,60,50]
english = [100,99,95,85]
percentage = []

for pair in zip(maths,science,english):
    rounded = round((sum(pair)/(len(pair)*100))*100,2)
    percentage.append(str(rounded)+'%')

print(percentage)