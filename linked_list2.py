class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class linked_list:
    def __init__(self):
        self.start = None
    def insert(self,value):
        newNode = Node(value)
        if(self.start == None):
            self.start = newNode
        else:
            temp = self.start
            while(temp.next != None):
                temp =temp.next
            temp.next = newNode
    def view(self):
        temp = self.start
        while(temp!=None):
            print(temp.value)
            temp=temp.next
list1 = linked_list()
list1.insert(2)
list1.insert(3)
list1.insert(2)
list1.insert(22)
list1.insert(23)
list1.insert(234)
list1.insert("aas")
list1.insert(22)
list1.insert(63)
list1.insert("sanjay")
list1.insert("3232")
list1.insert(33)
list1.view()
    
