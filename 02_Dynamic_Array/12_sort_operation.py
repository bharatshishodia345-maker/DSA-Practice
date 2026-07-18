# Dyanamic array

import ctypes

class my_list:
    def __init__(self):
        self.size = 1
        self.n = 0
    # creat a c type array with = self.size
        self.A = self.__make_array_(self.size)
    #Add len function
    def __len__(self):
        return self.n
    
    #print Array
    def __str__(self):
        result = ''
        for i in range(self.n):
            result = result+str(self.A[i]) + ','
        if self.n == 0:
            print("Data is clear")
        
        return '['+ result[:-1] + ']'
     
    #Indexing 
    def __getitem__(self,index):
         if 0<=index < self.n:
             return self.A[index]
         else:
             return 'Index error -> Index out of range ' 
            
    #Apend number
    def append(self, item):
        if self.n == self.size:
            #resize
            self.__resize(self.size*2)
        #append
        self.A[self.n] = item
        self.n = self.n + 1
    
    # Inserting operation
    def insert(self, pos,item):
        if self.n == self.size:
            self.__resize(self.size*2)
        for i in range(self.n,pos,-1):
            self.A[i] = self.A[i-1]
            
        self.A[pos] = item
        self.n = self.n+1
    #pop Item
    def pop(self):
        if self.n == 0:
            print("List Is Empty")
            
        print(self.A[self.n - 1])
        self.n = self.n-1
    
    # Delete element
    def __delitem__(self, pos):
        if 0<= pos <self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]               
            self.n = self.n-1
     
    # remove element
    def remove(self, item):
        pos = self.find(item)
        
        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos
                
    #Clear all Item
    def clear(self):
        self.size = 1
        self.n = 0
    
    #Find Item
    def find(self, item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return "ValueError -> Item not found"  
    
    def __resize(self, new_capacity):
        # create a new arr with new_capacity
        B = self.__make_array_(new_capacity)
        self.size =new_capacity
        # copy the content of A into B
        for i in range(self.n):
            B[i] = self.A[i]

        self.A = B
        
    def __make_array_(self, capacity):
        return(capacity*ctypes.py_object)()
    # sort array
    def sort(self):
        n = self.n
        for i in range(n):
            for j in range(n-i-1):
                if self.A[j] > self.A[j+1]:
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]
        return self
        
                    
    
new = my_list()


new.append(8)
new.append(2)
new.append(5)
new.append(6)
print(new)
new.sort()
print(new)
