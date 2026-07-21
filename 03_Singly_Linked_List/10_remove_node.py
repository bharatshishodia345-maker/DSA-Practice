# Add remove function 
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

    # Trevers linkedlist
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
    
    # Delete function
    def delete_head(self):
        if self.head == None:
            return '---Linked_list is Empty---'
        
        self.head = self.head.next
    
    # remove function 
    def remove(self,value):
        
        if self.head == None:
            return '---Linked_list is Empty'
        
        if self.head.data == value:
            self.delete_head()
            return
        
        curr = self.head
        
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
            
        if curr.next == None:
            return 'Item not found'
        else:
            curr.next = curr.next.next 
            self.n = self.n - 1
            
            

l = linked_list()
l.insert_head(1)
l.insert_head(2)
l.insert_head(3)
l.insert_head(6)

print(len(l))
print(l)
l.remove(300)
print(l)
     
        