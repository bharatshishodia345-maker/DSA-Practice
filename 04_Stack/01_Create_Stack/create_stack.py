# create new node in Stack


# Node class
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

#stack class
class stack:
    def __init__(self):
        self.top = None
    # isempty function (stack ==empty return true) else return false 
    def isempty(self):
        return self.top == None
    # push function add new node in stack 
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    # Traverse function print the stack data
    def traverse(self):
        temp = self.top

        while temp != None:
            print(temp.data)
            temp = temp.next

    
s = stack()


s.push(3)
s.push(2)
s.push(1)
s.traverse()

print(s.isempty())
