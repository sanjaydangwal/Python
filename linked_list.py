class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linkedList:
    def __init__(self):
        self.start = None
    def insert(self,value):
        newNode = Node(value)
        if self.start == None:
            self.start = newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp = temp.next
            temp.next = newNode
    def view(self):
        temp = self.start
        while(temp != None):
            print(temp.value,end = " ")
            temp = temp.next
list1 = linkedList()
list1.insert(2)
list1.insert(3)
list1.insert(5)
list1.insert(6)
list1.view()
