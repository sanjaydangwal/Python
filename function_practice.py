# def avrage_finder(*args):
#     avrage = []
#     for pear in zip(*args):
#         avrage.append(sum(pear)/len(pear))
    
#     return avrage


agv = lambda *args : [sum(pear)/len(pear) for pear in zip(*args)]
print(agv([1,2,3],[3,2,1],[2,1,3]))