# create a linked_list node and add Insert Function

class node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class linked_list:
    def __init__(self):
        self.head = None
        self.n = 0
        
    # length     
    def __len__(self):
        return self.n
    
    # insert new node
    def insert_head(self, value):
        # New node
        new_node = node(value)
        # create new conication
        new_node = self.head
        
        #resing head
        self.head = new_node
        
        # increment
        self.n = self.n + 1

l = linked_list()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(4)

print(len(l))
        
        