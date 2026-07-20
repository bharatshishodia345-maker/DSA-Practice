# create a linked_list node and check lenth of linklist 

class node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n

a = linked_list()
print(len(a))
        