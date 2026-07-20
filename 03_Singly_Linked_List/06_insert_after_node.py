# create a linked_list node and add insert_after function 

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

    # Treverse linkedlist
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]
    
    # Append new node 
    def append(self, value):
        new_node = node(value)
        
        if self.head == None:
            self.head=new_node 
            self.n = self.n+1
            return
        curr = self.head
        while curr.next != None:
            curr = curr.next
            
        curr.next = new_node
            
        self.n = self.n + 1
    # insert after a node    
    def insert_after(self, after,value ):
        new_node = node(value)
        
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
            
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
        else:
            return 'Value not found'
            
          
            

l = linked_list()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(6)

print(l)
l.insert_after(6,5)
print(l)
     
        