# create a linked_list node 

class node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0

a = linked_list()
a = node(1)
print(a)
        