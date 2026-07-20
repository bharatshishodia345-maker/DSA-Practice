# create a linked node and add treverse function

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
        new_node.next = self.head
        
        #resing head
        self.head = new_node
        
        # increment
        self.n = self.n + 1

    # Treverse linkedkedlist
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

l = linked_list()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(6)

print(len(l))

print(l)
     
        